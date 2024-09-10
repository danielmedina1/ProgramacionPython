def main():
    print("Hola Mundo")

def buenosDias(nombre):
    print("Buenos dias "+nombre)

def division (x, y):
    c = x//y
    r = x%y
    return c,r

if __name__ == "__main__":
    main()
    buenosDias(nombre = "Luis")
    print(division(x = 60, y = 6))