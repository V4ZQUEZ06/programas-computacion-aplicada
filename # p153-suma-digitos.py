# p153-suma-digitos.py
# Procesa una lista y crea otra con la suma de los dígitos de cada número

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

def suma_digitos(numero: int) -> int:
    numero = abs(numero)  # Por si hay números negativos
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma

def procesar_lista(lista: List[int]) -> List[int]:
    resultado = []
    for num in lista:
        resultado.append(suma_digitos(num))
    return resultado

# Programa principal
numeros = leer_lista()
lista_sumas = procesar_lista(numeros)

print("La lista de números original :", numeros)
print("La lista con las suma de dígitos de los números:", lista_sumas)
