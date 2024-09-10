def main():
    perfecto()
    
def perfecto():
    num = int (input("Introduzca un número: "))
    total = int(0)
    for i in range(num):
        if i != 0:
            if num % i == 0:
                total = total + i
    if num == total:
        print(f"El numero {num} es perfecto")
    else:
        print(f"El numero {num} no es perfecto")

if __name__ == "__main__":
    main()
    
