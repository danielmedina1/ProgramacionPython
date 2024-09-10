import socket

HOST = "127.0.0.1"
PORT = 2000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Conectado con exito")
b = True
while b:
    n = input("Introduce un numero del 1 al 10: ")
    while int(n) > 10 or int(n) < 0:
        n = input("El numero debe estar entre el 1 y el 10: ")

    #s.send("Soy el cliente: Daniel Medina".encode())
    s.send(n.encode())
    data = s.recv(1024)
    print(f"Recibo: {data.decode()}")

s.close()