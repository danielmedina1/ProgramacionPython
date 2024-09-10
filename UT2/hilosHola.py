import threading
import time

def imprimirMensaje(mensaje):
    for i in range(5):
        print(mensaje)
        time.sleep(1)

def main():
    hilo1 = threading.Thread(target = imprimirMensaje, args = ("Hilo1: Hola ",))
    hilo2 = threading.Thread(target = imprimirMensaje, args = ("Hilo2: mundo ",))
    
    hilo1.start()
    hilo2.start()
    
    hilo1.join()
    hilo2.join()
    
    print("FIN DE MAIN")



if __name__ == "__main__":
    main()