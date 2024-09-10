import subprocess

resultado = subprocess.run(["python", "UT1/suma.py", "9", "11"])

print(resultado.stderr)
print(resultado.returncode)