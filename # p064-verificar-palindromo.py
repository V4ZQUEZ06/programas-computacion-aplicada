# p064-verificar-palindromo.py
# Verificar si un número entero es palíndromo

while True:
    print('\033[H\033[J')  # Limpia pantalla
    print("Verificador de Números Palíndromos\n")

    # Entrada del número
    num = input("Introduce un número para verificar si es palíndromo: ")

    # Verificación
    if num == num[::-1]:
        print(f"El número {num} es un palíndromo.")
    else:
        print(f"El número {num} no es un palíndromo.")

    # Preguntar si continuar
    if input("\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\nFin del programa. ¡Gracias!")
