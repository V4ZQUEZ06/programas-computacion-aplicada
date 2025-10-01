# p059-pares-descendente.py
# Imprimir los números pares y su suma total en un rango descendente desde 100 hasta n

while True:
    print('\033[H\033[J')  # Limpia pantalla
    print("Imprimir los números pares y su suma total en un rango descendente")

    # Entrada validada
    while True:
        n = int(input("\nIntroduce un número límite (menor a 100): "))
        if n > 0 and n <= 100:
            break
        print("Error: El número debe ser positivo y menor o igual a 100.")

    # Inicialización
    pares = []
    suma = 0
    c = 100

    # Generar números pares descendentes y sumarlos
    while c >= n:
        if c % 2 == 0:
            pares.append(c)
            suma += c
        c -= 1

    # Resultados
    print("\nNúmeros pares:", ", ".join(map(str, pares)))
    print(f"La suma de los pares es: {suma}")

    # Preguntar si continuar
    if input("\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\nFin del programa. ¡Gracias!")
