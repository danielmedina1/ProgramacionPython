cifra = input("Digame cuantas palabras tiene la lista:  ")
i = int(0)
lista = []
while i < int(cifra):
    palabra = input(f"Digame la palabra {i+1}:  ")
    lista.append(palabra)
    i+=1

print(f"La lista creada es: {lista}")
    