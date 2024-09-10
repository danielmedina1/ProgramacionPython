num = input("Escriba un numero entero mayor a cero --- ")
if int(num) <= 0:
    num = input("Dije mayor a cero --- ")

fac = 1
i = int(num)
while int(i) > 0:
    fac = int(fac)*int(i)
    i = int(i)-1

print(f"El factorial de {num} es {fac}")