t = (1, "Hola", True)

print(t)

#Acceder a los elementos
print(t[0])

print(2 in t)

t = list(t)

print(t)

t = tuple(t)

print(t)

t1 = ("Rojo", "Verde")
print(t+t1)


print(len(t))

for color in t1:
    print(color)

#Conjuntos
set1 = set([1,1,2,2,2,3,4])
print(set1)

set1 = ("Hola", 2, True, 3, 3)

A = {1,3,5,2}
B = {2, 4, 6}

print(A.union(B))
print(A.intersection(B))
print(A-B)