import subprocess

resultado = subprocess.run(["python", "ejercicio3.py"], capture_output = True, text = True)

print(resultado.stdout)