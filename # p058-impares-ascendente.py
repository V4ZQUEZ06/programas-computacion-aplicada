# p058-impares-ascendente.py
# Imprimir los números impares y su suma total en un rango ascendente desde 1 hasta n

while True:
    print('\033[H\033[J')  # Limpia pantalla
    print("Imprimir los números impares y su suma total en un rango ascendente")

    # Entrada de datos
    n = int(input("\nIntroduce un número límite: "))

    # Inicialización
    impares = []
    suma = 0
    c = 1

    # Generar números impares y sumarlos
    while c <= n:
        if c % 2 != 0:
            impares.append(c)
            suma += c
        c += 1

    # Resultados
    print("\nNúmeros impares:", ", ".join(map(str, impares)))
    print(f"La suma de los impares es: {suma}")

    # Preguntar si desea continuar
    if input("\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\nFin del programa. ¡Gracias!")
