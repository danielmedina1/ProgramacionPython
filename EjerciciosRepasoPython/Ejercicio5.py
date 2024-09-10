def main():
    primos()
    
def primos():
    for i in range(1000):
        if i != 0:
            if esPrimo(i):
                print(i) 
    
def esPrimo(pnum):
    j = int(2)
    if pnum <= 1:
        return False
    for j in range(int(pnum)):
        if int(pnum) % int(j) == 0:
            return False
    return True

if __name__ == "__main__":
    main()
    
