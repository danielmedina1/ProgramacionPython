import random

print("JUEGO DE CARTAS")

c1 = random.randint(1,10)
c2 = random.randint(1,10)
c3 = random.randint(1,10)
c4 = random.randint(1,10)
c5 = random.randint(1,10)
c6 = random.randint(1,10)

print(f"Gloria ha sacado un {c1}, un {c2}, y un {c3}")
print(f"Héctor ha sacado un {c4}, un {c5} y un {c6}")

r1 = c1 + c2 + c3
r2 = c4 + c5 + c6

if r1 > r2 and r1 <= 15:
    print("Gloria gana")
else:
    if r1 < r2 and r2 <= 15:
        print("Héctor gana")
    else:
        if r1 == r2 and r1 <= 15 and r2 <= 15 :
            print("Empate")
        else:
            if r1 > 15:
                print("Héctor gana al no pasarse de 15")
            else:
                if r2 > 15:
                    print("Gloria gana al no pasarse de 15")
                else:
                    print("Ambos pierden al pasarse de 15")