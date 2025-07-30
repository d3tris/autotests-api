import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("localhost", 12345)
    server_socket.bind(server_address)

    server_socket.listen(5)
    print("Server waiting for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print("Connection from", {client_address})

        data = client_socket.recv(1024).decode()
        print("Received message:", data)

        response = f"Server received: {data}"
        client_socket.send(response.encode())

        client_socket.close()


if __name__ == '__main__':
    server()
