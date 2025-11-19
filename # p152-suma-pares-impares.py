# p152-suma-pares-impares.py
# Suma de números pares o impares dentro de un rango

def suma_rango(inicio: int, fin: int, tipo: str) -> int:
    suma = 0

    for numero in range(inicio, fin + 1):
        if tipo.upper() == 'P' and numero % 2 == 0:
            suma += numero
        elif tipo.upper() == 'I' and numero % 2 != 0:
            suma += numero

    return suma


print("*** Suma en Rango ***")

try:
    inicio = int(input("Introduce el número inicial: "))
    fin = int(input("Introduce el número final: "))
    tipo = input("¿Qué deseas sumar? (P)ares o (I)mpares: ").upper()

    if tipo not in ['P', 'I']:
        print("Error: Debes introducir 'P' para pares o 'I' para impares.")
    else:
        resultado = suma_rango(inicio, fin, tipo)

        if tipo == 'P':
            print(f"La suma de los números pares entre {inicio} y {fin} es: {resultado}")
        else:
            print(f"La suma de los números impares entre {inicio} y {fin} es: {resultado}")

except ValueError:
    print("Error: Debes ingresar números enteros para el rango.")
