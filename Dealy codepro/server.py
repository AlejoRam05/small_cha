"""
Conexion basica de un SERVIDOR
"""
import socket

PORT = 5000
HOST = "localhost"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

print("Server corriendo")

conn, direccion = server.accept()

data = conn.recv(1024).decode("utf-8") # 1024 limite de Bytes que puede leer

conn.send(data.encode("utf-8"))

server.close()
print("conexion cerrada")
