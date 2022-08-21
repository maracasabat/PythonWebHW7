import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 9001


def run_client(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        server = ip, port
        client_socket.connect(server)
        message = input('--> ')

        while message.lower().strip() != 'bye':
            client_socket.send(message.encode())
            data = client_socket.recv(1024)
            print(f'\033[035m Received message: {data.decode()}\033[0m')
            message = input('--> ')

        print('Ok')


if __name__ == '__main__':
    run_client(TCP_IP, TCP_PORT)
