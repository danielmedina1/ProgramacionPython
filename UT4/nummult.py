def fichero_tabla(n):
    nombre = 'UT4/tabla'+str(n)+'.txt'
    fichero = open(nombre, 'w')
    for i in range(1, 11):
        fichero.write(str(i)+' x '+str(n)+' = '+str(i*n)+'\n')
        
    fichero.close()


if __name__ == "__main__":
    n = int(input('Dame un número: '))
    fichero_tabla(n)