import random
print("JUEGO DE DADOS")
d1 = random.randint(1,6)
d2 = random.randint(1,6)
print(f"Alvaro ha sacado un {d1}")
print(f"Barbara ha sacado un {d2}")

if d1 > d2:
    print("Alvaro gana")
else:
    if d1 < d2:
        print("Barbara gana")
    else:
        print("Empate")