import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("localhost", 12345)
    server_socket.bind(server_address)

    server_socket.listen(10)
    print("Server running and waiting for connections...")
    messages: list[str] = []
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"User with address: {client_address} connected to server")

        message = client_socket.recv(1024).decode()
        print(f"User with address: {client_address} sent message: {message}")
        messages.append(message)

        client_socket.send('\n'.join(messages).encode())
        client_socket.close()


if __name__ == '__main__':
    server()
