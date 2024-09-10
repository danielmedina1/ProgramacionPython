import subprocess

resultado = subprocess.run(["python", "timer.py", "9"])

print(resultado.stderr)
print(resultado.returncode)