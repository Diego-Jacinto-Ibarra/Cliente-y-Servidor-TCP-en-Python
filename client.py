import socket

def main():
    host = 'localhost'
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Ingrese un mensaje: ")

        client_socket.sendall(message.encode())

        if message == '':
            print("No se ha ingresado ningún mensaje")
            continue

        if message == "DESCONEXION":
            print("Cerrando la conexión...")
            break

        response = client_socket.recv(1024).decode()
        print(f"Respuesta del servidor: {response}")

    client_socket.close()

if __name__ == "__main__":
    main()