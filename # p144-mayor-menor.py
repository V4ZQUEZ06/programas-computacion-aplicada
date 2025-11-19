# p144-mayor-menor.py
# Funciones para encontrar el número mayor y menor en una lista de números,
# junto con la captura de datos desde la entrada estándar.

from typing import List

def mayor(lista: List[float]) -> float:
    mayor_num = lista[0]
    for numero in lista:
        if numero > mayor_num:
            mayor_num = numero
    return mayor_num

def menor(lista: List[float]) -> float:
    menor_num = lista[0]
    for numero in lista:
        if numero < menor_num:
            menor_num = numero
    return menor_num

def captura_datos() -> List[float]:
    datos = []
    print("Ingresa números (escribe 'fin' para terminar):")
    while True:
        entrada = input("Número: ")
        if entrada.lower() == 'fin':
            break

        try:
            numero = float(entrada)
            datos.append(numero)
        except ValueError:
            print("Por favor, ingresa un número válido o 'fin' para terminar.")
    return datos

# Ejemplo de uso
numeros = captura_datos()
if numeros:
    num_mayor = mayor(numeros)
    num_menor = menor(numeros)
    print(f'Total de números ingresados: {len(numeros)}')
    print(f"El número mayor es: {num_mayor}")
    print(f"El número menor es: {num_menor}")
else:
    print("No se ingresaron números.")
