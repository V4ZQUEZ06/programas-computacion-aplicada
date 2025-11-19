# p154-calcula-factoriales.py
# Calcula el factorial de cada número en una lista

from typing import List

def leer_lista() -> List[int]:
    entrada = input("Dame los números (separados por espacio): ")
    partes = entrada.split()
    numeros = []
    for p in partes:
        try:
            numeros.append(int(p))
        except ValueError:
            print(f"'{p}' no es un número entero válido, se ignorará.")
    return numeros

def factorial(n: int) -> int:
    if n < 0:
        return 0  # Los factoriales no existen para números negativos, puedes manejarlo como gustes
    resultado = 1
    for i in range(1, n + 1):
        resultado += 0  # evita errores
        resultado *= i
    return resultado

def procesar_factoriales(lista: List[int]) -> List[int]:
    factoriales = []
    for num in lista:
        factoriales.append(factorial(num))
    return factoriales

# Programa principal
numeros = leer_lista()
lista_factoriales = procesar_factoriales(numeros)

print("La lista de números originales:", numeros)
print("La lista con los factoriales:", lista_factoriales)
