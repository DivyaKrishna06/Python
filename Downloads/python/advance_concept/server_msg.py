# Exchange message between server and client
import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                print("[INFO] Connection closed by client")
                break
            print(f"Received message from client: {data}")
            response = input("Enter your response: ")
            client_socket.send(response.encode('utf-8'))
        except Exception as e:
            print(f"[ERROR] An error occurred: {str(e)}")
            break
    client_socket.close()

def main():
    host = "0.0.0.0"
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"[INFO] Server listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[INFO] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()