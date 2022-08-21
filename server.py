import socket
from concurrent import futures

TCP_IP = '127.0.0.1'
TCP_PORT = 9001


def run_server(ip, port):
    def handle_server(conn):
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f'\033[035m Received message: {data.decode()}\033[0m')
            message = input('--> ')
            conn.send(message.encode())
        print('Ok')
        conn.close()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = ip, port
    server_socket.bind(server)
    server_socket.listen(10)
    with futures.ThreadPoolExecutor(max_workers=10) as executor:
        try:
            while True:
                conn, address = server_socket.accept()
                executor.submit(handle_server, conn)
                print(f'Connection from: {address}')
        except KeyboardInterrupt:
            print('Server stopped')
        finally:
            server_socket.close()


if __name__ == '__main__':
    run_server(TCP_IP, TCP_PORT)
