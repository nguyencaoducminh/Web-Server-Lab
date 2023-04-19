#import socket module
from socket import *
from  _thread import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverPort = 12345
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

def threaded_client(connectionSocket):
    while True:
        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()

            #Send one HTTP header line into socket
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
            break
        except IOError:
            #Send response message for file not found
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())

            #Close client socket
            connectionSocket.close()
            break

print('Ready to serve...')
while True:
    #Establish the connection
    connectionSocket, addr = serverSocket.accept()
    if connectionSocket:
        start_new_thread(threaded_client, (connectionSocket,))
    

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data