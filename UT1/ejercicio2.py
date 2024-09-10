import subprocess
#Tambien se puede usar la ruta directa
try:
    subprocess.run(["Notepad.exe"])
except subprocess.CalledProcessError as e:
    print(e.output)