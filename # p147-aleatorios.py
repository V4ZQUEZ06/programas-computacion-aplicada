# p147-aleatorios.py
# Generar una lista de números aleatorios dentro de un rango dado por el usuario

import random
from typing import List

def generar_aleatorios(cantidad: int, minimo: int, maximo: int) -> List[int]:
    lista = []
    for _ in range(cantidad):
        lista.append(random.randint(minimo, maximo))
    return lista

# Ejemplo interactivo de uso
print("=== Generador de números aleatorios ===")
try:
    n = int(input("¿Cuántos números aleatorios deseas generar?: "))
    a = int(input("Ingresa el valor mínimo: "))
    b = int(input("Ingresa el valor máximo: "))

    if n <= 0:
        print("La cantidad debe ser mayor que cero.")
    elif a > b:
        print("El mínimo no puede ser mayor que el máximo.")
    else:
        resultado = generar_aleatorios(n, a, b)
        print(f"Números generados: {resultado}")

except ValueError:
    print("Debes ingresar valores numéricos enteros.")
