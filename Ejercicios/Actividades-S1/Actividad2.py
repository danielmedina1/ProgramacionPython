import random
print("JUEGO DE DADOS DOBLES")

d1 = random.randint(1,6)
d2 = random.randint(1,6)
d3 = random.randint(1,6)
d4 = random.randint(1,6)

print(f"David ha sacado un {d1}, y un {d2}")
print(f"Carmen ha sacado un {d3}, y un {d4}")

r1 = d1 + d2
r2 = d3 + d4

if r1 > r2:
    print("David gana")
else:
    if r1 < r2:
        print("Carmen gana")
    else:
        print("Empate")