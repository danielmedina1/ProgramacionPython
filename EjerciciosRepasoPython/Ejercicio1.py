num = int (input("Introduzca un número: "))

for i in range(num+1):
    if i != 0:
        if num % i == 0:
            print(i)