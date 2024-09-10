import subprocess

def main():
    comandos()

def comandos():
    comando = input("Introduce un comando:  ")
    
    proc = subprocess.run([comando], shell = True, capture_output = True, text = True)
    if proc.returncode > 0:
        print("Ejecucion Inexitosa")
        print(proc.stderr)
    else:
        print("Ejecucion Exitosa")
        print(proc.stdout)

if __name__ == "__main__":
    main()

