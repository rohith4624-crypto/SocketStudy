import socket

s = socket.socket()
s.connect(('localhost', 8000))
print("Connected to server!")

while True:
    data = s.recv(1024).decode()
    if not data:
        break
    print("Server:", data)
    s.send("Acknowledgement Received".encode())

s.close()