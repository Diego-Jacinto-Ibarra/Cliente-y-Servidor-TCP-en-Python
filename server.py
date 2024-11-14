import socket

def main():
    host = 'localhost'
    port = 5000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f'Servidor escuchando en {host}:{port}')

    while True:
        client_socket , address = server.accept()
        print(f'Conexion establecida con: {address}')

        while True:
            data = client_socket.recv(1024).decode()

            if not data:
                break

            if data == 'DESCONEXION':
                print('Servidor cierra la conexión con el cliente...')
                client_socket.close()
                break

            else:
                response = data.upper()
                client_socket.send(response.encode())

if __name__ == '__main__':
    main()