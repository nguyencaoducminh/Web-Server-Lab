from socket import *
import sys

connectionSocket = socket(AF_INET, SOCK_STREAM)

host = sys.argv[1]
port = int(sys.argv[2])
filename = sys.argv[3]

connectionSocket.connect((host, port))

message = "GET /" + filename + " HTTP/1.1\r\n\r\n"

connectionSocket.sendall(message.encode())

data = []

while True:
    chunk = connectionSocket.recv(4096)
    if chunk:
        data.append(chunk.decode())
    else:
        break

print("".join(data))
