import socket
HOST = '0.0.0.0'
PORT = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("Controller running... waiting for authentication")
while True:
    conn, addr = server.accept()
    print(f"Connection from {addr}")
    data = conn.recv(1024).decode()
    if data == "AUTH_SUCCESS":
        print("✅ Identity Verified → Flow Rule Installed")
        print("🔓 Gateway OPENED for user")
    conn.close()