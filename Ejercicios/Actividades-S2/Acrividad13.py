num = input("Introduzca un numero --- ")

divs = 0
i = 1

for i in range(9):
    if int(num)%int(i) == 0:
        div = int(div)+1
    i = int(i)+1

if divs > 2:
    print("El numero es primo")

else:
    print("El numero no es primo")