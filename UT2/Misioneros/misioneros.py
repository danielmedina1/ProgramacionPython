import threading
import time

class Olla:
    def __init__(self):
        self.lock = threading.Lock()
        self.contenido = []

    def agregar_misionero(self, misionero):
       with self.lock:
            self.contenido.append(misionero)
            print(f"Se ha agregado un misionero a la olla. Contenido: {self.contenido}")

    def comer_misionero(self, canibal):
        with self.lock:
          #Mientras esté vacío espera


            print(f"{canibal} ha comido a un misionero. Contenido restante: {self.contenido}")



def canibal(id, olla):
   #crear 3 caníbales y llamar al método comer de Olla
   x = 1

def cocinero(olla):
    #Cocinar n misioneros
    x = 1

def main():
    olla = Olla()

    # Creamos hilos para los caníbales
    hilos_canibales = []
   

    # Creamos el hilo para el cocinero
    hilo_cocinero = []

    # Iniciamos los hilos
   

    # Esperamos a que todos los hilos terminen
  

if __name__ == "__main__":
    main()