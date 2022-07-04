"""
- Un entorno virtual
py -m venv entorno
entorno/Scripts/Activate.ps1

- Archivos de dependencias

python -m pip install ./requirements-dev.txt

- Un modulo de operaciones matematicas
- Una suite de tests

python -m pytest

- Desactivar

deactivate

"""

def sumar(a, b):
    return a + b

def multiplicar(a, b):
    total = 0
    for i in range(0, b):
        total = sumar(total, a)
    return total
