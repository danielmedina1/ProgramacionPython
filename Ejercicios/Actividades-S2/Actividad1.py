print("PARES E IMPARES")
num = input("Escriba un número entero: ")
num2 = input(f"Escriba un número entero mayor o agual a {num}: ")

if num2 < num:
    while num2 < num:
        num2 = input(f"Le he dicho que tiene que ser mayor o igual a {num}: ")
i = num
i2 = int(num2)
for i in range(i2):
    if i%2 == 0:
        print(f"El numero {i} es par")
    else:
        print(f"El numero {i} es impar")
    
