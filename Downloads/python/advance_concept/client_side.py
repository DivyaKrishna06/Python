import socket

s = socket.socket()

port = 40674 # Port to connect

#Connect to local server
s.connect(('127.0.0.1', port))

# receive data from the server
print(s.recv(1024))

s.close()