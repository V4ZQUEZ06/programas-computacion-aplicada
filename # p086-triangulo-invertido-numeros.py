# p086-triangulo-invertido-numeros.py
# Imprime un triángulo numérico invertido.
# RESTRICCIONES: usar únicamente if, while, for (sin arreglos/listas, sin funciones, sin POO).

print('\033[H\033[J', end='')
print('--- Triángulo numérico invertido ---\n')

# --- Entrada ---
n = int(input("Dame un número: "))

print()  # línea en blanco

# --- Si n es menor que 1, no hay nada que dibujar ---
if n < 1:
    print("Nada que imprimir (n debe ser >= 1).")
else:
    # Bucle de filas: desde n hasta 1
    fila = n
    while fila >= 1:
        # Bucle de columnas: imprime 1 2 3 ... fila
        col = 1
        while col <= fila:
            # Imprimir con espacio entre números (sin espacio inicial al principio)
            if col == 1:
                print(col, end="")
            else:
                print(" " + str(col), end="")
            col = col + 1
        print()  # salto de línea al terminar la fila
        fila = fila - 1
