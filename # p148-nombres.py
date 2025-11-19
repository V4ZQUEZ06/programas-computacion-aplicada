# p148-nombres.py
# Escribe una función que tome dos listas de nombres, las una,
# invierta el orden y convierta todos los nombres a mayúsculas.

from typing import List

def une_procesa(lista1: List[str], lista2: List[str]) -> List[str]:
    nombres_unidos = lista1 + lista2
    nombres_invertidos = nombres_unidos[::-1]
    nombres_mayusculas = []
    for nombre in nombres_invertidos:
        nombres_mayusculas.append(nombre.upper())
    return nombres_mayusculas

def entrada() -> List[str]:
    datos = []
    print("Introduce nombres (deja en blanco para terminar):")
    while True:
        nombre = input("Nombre: ")
        if nombre == "":
            break
        datos.append(nombre)
    return datos

# Ejemplo de uso
nombres1 = ["Ana", "Luis", "Carlos", "Marta", "Sofía"]
nombres2 = entrada()
nombres_procesados = une_procesa(nombres1, nombres2)
print(f"Nombres procesados: {nombres_procesados} - fueron: {len(nombres_procesados)}")
