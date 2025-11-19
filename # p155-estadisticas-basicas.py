# p155-estadisticas-basicas.py
# Cálculo de estadísticas básicas poblacionales para una lista de números

from typing import List
import math

def leer_lista() -> List[int]:
    entrada = input("Dame números (separados por espacio): ")
    partes = entrada.split()
    numeros = []
    for p in partes:
        try:
            numeros.append(int(p))
        except ValueError:
            print(f"'{p}' no es un número válido y se ignorará.")
    return numeros

def mayor(lista: List[int]) -> int:
    m = lista[0]
    for n in lista:
        if n > m:
            m = n
    return m

def menor(lista: List[int]) -> int:
    m = lista[0]
    for n in lista:
        if n < m:
            m = n
    return m

def media(lista: List[int]) -> float:
    return sum(lista) / len(lista)

def varianza_poblacional(lista: List[int]) -> float:
    mu = media(lista)
    suma = 0
    for x in lista:
        suma += (x - mu) ** 2
    return suma / len(lista)

def desviacion_poblacional(lista: List[int]) -> float:
    return math.sqrt(varianza_poblacional(lista))

# ----------- PROGRAMA PRINCIPAL -----------

numeros = leer_lista()

print("Lista de números:", numeros)
print("Estadísticas:")

print(f"Media : {media(numeros):.3f}")
print(f"Mayor : {mayor(numeros)}")
print(f"Menor : {menor(numeros)}")
print(f"Varianza : {varianza_poblacional(numeros):.3f}")
print(f"Desviación estándar: {desviacion_poblacional(numeros):.3f}")
