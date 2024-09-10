cant = int(0)
cant = input("¿Cuantos numeros va a meter? --- ")
suma = float(0.0)
i = int(0)
while int(i) < int(cant):
    num = float(input("Introduce los numeros --- "))
    suma = suma + num
    i = i + 1

print(f"La suma de esos numeros es {suma}")