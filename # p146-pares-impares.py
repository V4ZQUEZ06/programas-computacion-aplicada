# p146-pares-impares.py
# Escribe una función que tome una lista de números y devuelva dos listas:
# una con los números pares y otra con los números impares.

from typing import List, Tuple

def separar_pares_impares(lista: List[int]) -> Tuple[List[int], List[int]]:
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = separar_pares_impares(numeros)
print(f"Números pares: {pares} - fueron: {len(pares)}")
print(f"Números impares: {impares} - fueron: {len(impares)}")
