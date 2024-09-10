cant = int(0)
cant = input("¿Cuantos numeros va a meter? --- ")
suma = float(0.0)
max = 0
min = 10000000000
media = 0
i = int(0)
while int(i) < int(cant):
    num = float(input("Introduce los numeros --- "))
    suma = suma + num
    i = i + 1
    if int(num) > max:
        max = int(num)
    if int(num) < min:
        min = int(num)
media = int(suma)/int(cant)
print(f"La suma de esos numeros es {suma}")
print(f"El número mas grande es {max}")
print(f"El número mas pequeño es {min}")
print(f"La media de esos números es {media}")
