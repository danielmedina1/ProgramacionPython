num1 = input("Introduzca un numero:  ")
num2 = input("Introduzca otro numero:  ")
suma = 0

if num1 > num2:
    i = int(num2)+1
    print(f"La suma de los numeros entre {num2} y {num1} es:")
    while int(i) < int(num1):
        suma = int(suma)+int(i)
        i = int(i)+1
    print(suma)
elif num2 > num1:
    i = int(num1)+1
    print(f"La suma de los numeros entre {num1} y {num2} es:")
    while int(i) < int(num2):
        suma = int(suma)+int(i)
        i = int(i)+1
    print(suma)
else:
    print(f"La suma de los numeros entre {num1} y {num2} es 0")