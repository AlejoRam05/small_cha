import socket

PORT = 5000
HOST = "localhost"

# Connect client to Server
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((HOST, PORT))

mensaje = "Hello world!"
cliente.sendall(mensaje.encode("utf-8"))

recibido = cliente.recv(1024).decode("utf-8")
print(recibido)

cliente.close()
print("conexion cerrada")
