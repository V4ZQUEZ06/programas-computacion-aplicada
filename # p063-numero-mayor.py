# p063-numero-mayor.py
# Leer una serie de números hasta que el usuario ingrese un 0
# Mostrar cuál fue el número mayor de todos los introducidos

while True:
    print('\033[H\033[J')  # Limpia pantalla
    print("Lectura de números (0 para terminar)\n")

    mayor = None  # No hay número aún

    while True:
        num = float(input("> "))
        if num == 0:
            break
        if mayor is None or num > mayor:
            mayor = num

    # Resultados
    print("-" * 20)
    if mayor is not None:
        print(f"El número mayor fue: {mayor}")
    else:
        print("No se introdujeron números distintos de 0.")

    # Preguntar si desea continuar
    if input("\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\nFin del programa. ¡Gracias!")
