# p061-suma-200.py
# Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200.

while True:
    print('\033[H\033[J')  # Limpia pantalla
    print("Sumador hasta alcanzar 200\n")

    suma = 0
    contador = 0

    while suma < 200:
        num = float(input(f"Suma actual: {suma}. Introduce un número: "))
        suma += num
        contador += 1

    # Resultados
    print("-" * 20)
    print("Meta de 200 alcanzada.")
    print(f"Suma final: {suma}")
    print(f"Total de números introducidos: {contador}")

    # Preguntar si desea continuar
    if input("\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\nFin del programa. ¡Gracias!")
