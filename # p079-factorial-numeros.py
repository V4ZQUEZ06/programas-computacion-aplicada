# p079-factorial-numeros.py
# Calcula el factorial de los números desde 1 hasta n

print('\033[H\033[J', end='')
print("--- Cálculo Sucesivo de Factoriales ---\n")

try:
    n = int(input("¿Hasta qué número deseas calcular el factorial? "))
    if n < 1:
        print("Por favor, ingresa un entero positivo (>= 1).")
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
            print(f"{i}! = {factorial}")
except ValueError:
    print("Error: Por favor, introduce un número entero válido.")
