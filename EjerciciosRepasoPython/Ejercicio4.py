def main():
    num = 1
    while num >= 0:
        num = int (input("Introduzca un número: "))
        if num >= 0:
            divisores(num)
    
def divisores(num):
    total = int(0)
    for i in range(num):
        if i != 0:
            if num % i == 0:
                total = total + i
    print(f"La sumas de los divisores de {num} es {total}")

if __name__ == "__main__":
    main()
    
