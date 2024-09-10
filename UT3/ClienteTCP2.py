import socket

HOST = "192.168.21.100"
PORT = 2000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Conectado co exito")
s.send("Soy el cliente: Daniel Medina".encode())
data = s.recv(1024)
print(f"Recibo: {data.decode()}")

s.close()