#Comentario con almohadilla
import keyword 
print (keyword.kwlist)
import math

x = 1
print(x)

x= "Hola como estas"
print(x)

nombre, edad = "Marta", 23
print("Nombre: ", nombre)
print("Edad: ", edad)
print(f"Tu nombre es {nombre} y tu edad es {edad}")
print(f"Tu nombre es",nombre,"y tu edad es",edad)
print("")
#Operaciones aritmeticas
x = 3 + 1
print(x)
x= x+5
print(x)
x+=3
print(x)
x = 7
print(type(x))
x = 3.14
print(type(x))
#Datos por Teclado
x = input("Dame un número: ")
print(f"El número es: {x}")
#Funciones
y = input("Dame un número decimal: ")
print(f"El número redondeado es: {round (float(y),1)}")
#Cociente y Resto
cociente = 15//2
resto = 15%2
print(cociente)
print (resto)
#Potencias
pot = pow(2, 3)
print (pot)
#Valor Absoluto
print ("El valor absoluto es: ", abs(-9))
#El máximo
print(f"El máximo número entre 0, 5, 6, 3 es {max(0,5,6,3)}")
#suma
#print(f"La suma de 1,2,3,4,5,6,7,8,9 es {sum(1,2,3)}")
palabra = "Hola buenas tardes"
print(palabra[-5]) 
