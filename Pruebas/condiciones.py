import random
x = int(input("Introduzca su edad: "))

if x >= 18 and x <= 64:
    print("Puedes Trabajar")
elif x < 18:
    print("Eres Menor de Edad")
else :
    print("Estas jubilado")


palabra = str(input("Escribe una palabra: "))
if palabra.startswith("S") or palabra.startswith("s"):
    print("La palabra empieza con S")
else :
    print("La palabra no empieza con S")

y = random.randint(1, 101)
print(y)