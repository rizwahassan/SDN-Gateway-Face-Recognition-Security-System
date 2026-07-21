import streamlit as st
import socket
import cv2
import numpy as np
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("model.yml")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
def recognize_face(img_bytes):
    file_bytes = np.frombuffer(img_bytes.getvalue(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    img = cv2.flip(img, 1)
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces) == 0:
        return False, 0
    (x, y, w, h) = faces[0]
    face = gray[y:y+h, x:x+w]
    face = cv2.resize(face, (200, 200))
    label, confidence = recognizer.predict(face)
    match = confidence < 70
    score = 100 - confidence
    return match, score
if "auth" not in st.session_state:
    st.session_state.auth = False
st.title("BioNet SDN Gateway ")
if st.session_state.auth:
    st.success("🔓 GATEWAY OPEN")
else:
    st.error("🔒 GATEWAY LOCKED")
mode = st.radio("Input", ["Camera", "Upload"])
img = None
if mode == "Camera":
    img = st.camera_input("Scan Face")
else:
    img = st.file_uploader("Upload", type=["jpg", "png"])
if img:
    match, score = recognize_face(img)
    if match and score > 30:   
        st.success(f"Identity Verified (Score: {int(score)}%)")
        if st.button("OPEN GATE"):
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(2)
                client.connect(('192.168.1.6', 9999))
                client.send(b"AUTH_SUCCESS")
                client.close()
            except:
                pass
            st.session_state.auth = True
            st.rerun()
    else:
        st.error(f"Access Denied (Score: {int(score)}%)")
        st.session_state.auth = False