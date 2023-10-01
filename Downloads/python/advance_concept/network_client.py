import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port to connect to
server_address = ('localhost', 8888)

# Connect to the server
client_socket.connect(server_address)

# Send data to the server
message = "Hello from the client!"
client_socket.send(message.encode('utf-8'))

# Receive a response from the server
response = client_socket.recv(1024).decode('utf-8')
print(f"Received from server: {response}")

# Close the client socket
client_socket.close()