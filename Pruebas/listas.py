#Listas
l = ["Hola", 1, True]
print(l)

#Tamaño de la lista
print(len(l))

#Elementos
names = ["Paco", "Luis", "Marta", "Jaime"]
print(names[3])
print(names[-1])

print(names[1:3]) #sin incluir el ultimo
print(names[:3]) #Del 0 al x sin incluir el ultimo

#Funciones
names.append("Adrian")
print(names)
names.insert(1, "Lucia")
print(names)

names2 = ["Olivia", "Hector"]
names3 = names + names2

print(names3)

#Recorrer
for i in range(len(names)):
    print(names[i], end=" ")

for name in names:
    print(name, end=" ")

#Count cuenta cuantas veces hay un determinado elemento en una lista
numbers = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3]
counted = []
for element in numbers:
    if element not in counted:
        counted.append(element)
        print(f"El elemento {element} aparece {numbers.count(element)}")


#Ordenar una lista
numbers2 = [1, 7, 3, 9, 4, 7, 4, 8, 2, 9, 19]
print(numbers2)
numbers2.sort()
print(numbers2)

#Lista al revés
numbers.reverse()
print(numbers)

#Borrar en una posicion
print(numbers)
del numbers[0]
print(numbers)

#Borrarla primera aparicion del elemento en la lista
numbers.remove(3)
print(numbers)

numeros = list(range(0, 100, 2))
print(numeros)

matriz = [1, 2, [3, 4]]

