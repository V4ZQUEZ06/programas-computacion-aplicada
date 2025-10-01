# p060-promedio-suma.py
# Leer números introducidos por el usuario hasta que ingrese un 0.
# Al finalizar, mostrar el conteo, la suma y el promedio.

while True:
    print('\033[H\033[J')  # Limpia pantalla
    print("Lectura de números (0 para terminar)\n")

    numeros = []
    while True:
        num = float(input("> "))
        if num == 0:
            break
        numeros.append(num)

    # Procesar resultados
    cantidad = len(numeros)
    suma = sum(numeros)
    promedio = suma / cantidad if cantidad > 0 else 0

    print("-" * 20)
    print(f"Se introdujeron {cantidad} números.")
    print(f"La suma es: {suma}")
    print(f"El promedio es: {promedio:.2f}")

    # Preguntar si desea continuar
    if input("\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\nFin del programa. ¡Gracias!")
