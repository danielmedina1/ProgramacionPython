import socket
import random

HOST = "127.0.0.1"
PORT = 2000
intentos = int(4)
n =int(random.randint(1, 10)) 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while intentos != 0:
    conn, addr = s.accept() #espera al cliente
    num = conn.recv(1024)
    n2 = num.decode()
    print("El numero recibido es: ", n2)
    if int(n2) == int(n):
        print(f"Has ganado, el numero era: {n}")
        conn.close()
    else :
        if int(n2) > n:
            conn.send("El numero debe ser menor".encode())
            intentos = int(intentos) - 1
        if int(n2) < n:
            conn.send("El numero debe ser mayor".encode())
            intentos = int(intentos) - 1

    
conn.close()