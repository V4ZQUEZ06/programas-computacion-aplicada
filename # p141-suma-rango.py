# p141-suma-rango.py
# Dado el inicio y fin, regresa la suma de números en el rango especificado.

def suma_rango(inicio: int, fin: int) -> int:
    suma = 0
    for numero in range(inicio, fin + 1):
        suma += numero
    return suma

def main() -> None:
    inicio = int(input("Introduce el inicio del rango: "))
    fin = int(input("Introduce el fin del rango: "))
    resultado = suma_rango(inicio, fin)
    print(f"La suma de los números en el rango de {inicio} a {fin} es {resultado}")

if __name__ == "__main__":
    main()
