def main():
    divisores()
    
def divisores():
    num = int (input("Introduzca un número: "))
    total = int(0)
    for i in range(num):
        if i != 0:
            if num % i == 0:
                total = total + i
    print(f"La sumas de los divisores de {num} es {total}")

if __name__ == "__main__":
    main()
    
