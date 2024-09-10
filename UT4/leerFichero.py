fichero = open('UT4/ejemplo.txt', 'r')
#print(fichero.read())
linea = fichero.readline()
while linea != '':
    print(linea+'|-|', end='')
    linea = fichero.readline()
fichero.close()
