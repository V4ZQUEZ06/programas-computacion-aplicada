# p053-conjetura-collatz.py
# Calcula la conjetura de Collatz

while True:
    print('\033[H\033[J')  # Limpia pantalla en terminal compatible
    print("Imprime la conjetura de Collatz")

    # Validar entrada
    while True:
        num = int(input("Dame un número = "))
        if num > 0:
            break
        print("Error, el número debe ser mayor que 0")

    # Mostrar la secuencia
    print("\nLa conjetura de Collatz es:")
    while True:
        print(num, end=" ")
        if num == 1:
            break
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1

    # Preguntar si continuar
    res = input("\n\n¿Deseas Continuar (S/N)? ").upper()
    if res == "N":
        break

print("\nGracias por usar este programa. Vuelve pronto.")
