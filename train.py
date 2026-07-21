import cv2
import os
import numpy as np
recognizer = cv2.face.LBPHFaceRecognizer_create()
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
dataset_path = "dataset"
faces = []
labels = []
print("Training started...")
for file in os.listdir(dataset_path):
    img_path = os.path.join(dataset_path, file)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        continue
    detected = face_cascade.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in detected:
        face = img[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))
        faces.append(face)
        labels.append(1)  
if len(faces) == 0:
    print("❌ No faces found in dataset")
    exit()
recognizer.train(faces, np.array(labels))
recognizer.save("model.yml")
print(" Training complete. model.yml created")