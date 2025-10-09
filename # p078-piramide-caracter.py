# p078-piramide-caracter.py
# Imprime una pirámide de caracteres

print('\033[H\033[J', end='')
print('Imprime una pirámide de caracteres')

# Lectura segura de la altura
while True:
    try:
        altura = int(input("Introduce la altura de la pirámide: "))
        if altura <= 0:
            print("Ingresa un entero positivo.\n")
            continue
        break
    except ValueError:
        print("Entrada no válida. Escribe un entero.\n")

car = input("Introduce el carácter para la pirámide: ")
car = (car.strip() or "*")[0]  # usa '*' si está vacío; solo primer carácter

print("\n--- Pirámide Generada ---")

# Bucle exterior para cada nivel de la pirámide
for i in range(1, altura + 1):
    # Calcular espacios y caracteres para el nivel actual
    espacios = altura - i
    caracteres = 2 * i - 1

    # Imprimir los espacios en blanco a la izquierda
    for _ in range(espacios):
        print(" ", end="")

    # Imprimir los caracteres
    for _ in range(caracteres):
        print(car, end="")

    # Salto de línea para pasar al siguiente nivel
    print()
