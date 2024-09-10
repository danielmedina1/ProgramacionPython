import socket

HOST = "127.0.0.1"
PORT = 2000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept() #espera al cliente
print(f"Conexión con el cliente, IP: {addr[0]} y Puerto: {addr[1]}")

conn.close()