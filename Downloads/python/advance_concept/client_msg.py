# Exchange message between client and server
import socket

def main():
    host = "127.0.0.1"
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        message = input("Enter your message (type 'exit' to quit): ")
        if message == 'exit':
            break
        client.send(message.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(f"Received response from server: {response}")

    client.close()

if __name__ == "__main__":
    main()