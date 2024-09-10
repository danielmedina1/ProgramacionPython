def main():
    menu()
    op = 0
    op2 = 0
    op3 = 0
    while op not in (1, 2, 3):
        print("Seleccione una opcion")
        op = int(input())
    
    sueldo = asignarSueldo(op)

    while op2 <= 0:
        print("¿Cuantas veces ha viajado?")
        op2 = int(input())
    while op3 not in (1, 2): 
        print("Introduzca su estado civil (1 - Soltero | 2 - Casado)")
        op3 = int(input())
    cas = estadoCivil(op3)
    
    viajes = int(op2) * int(30)
    sbruto = int(sueldo) + int(viajes)
    retencion = float(sbruto) * float(cas)
    neto = float(sbruto) - float(retencion)
    print("------------------------------------------------")
    print(f"Sueldo base: {sueldo}")
    print(f"Dietas ({op2} viajes): {viajes}")
    print("------------------------------------------------")
    print(f"Sueldo bruto: {sbruto}")
    print(f"Retencion IRPF: {retencion}")
    print("------------------------------------------------")
    print(f"Sueldo Neto: {neto}")
    print("------------------------------------------------")
    
    
def menu():
    print("*****************************************")
    print("Calculo de nomina")
    print("*****************************************")
    print("1)Programador Junior")
    print("2)Programador Senior")
    print("3)Jefe de Proyecto")
    print("*****************************************")

def asignarSueldo(op):
    sueldo = 0
    if op == 1:
        sueldo = 950
    if op == 2:
        sueldo = 1200
    if op == 3:
        sueldo = 1600
    return sueldo

def estadoCivil(op3):
    cas = 0
    if op3 == 1:
        cas = 25/100
    if op3 == 2:
        cas = 20/100
    return cas

if __name__ == "__main__":
    main()