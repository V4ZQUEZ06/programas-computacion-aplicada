# p084-cuadro-hueco-caracter.py
# Dibuja un cuadrado hueco con el carácter indicado.
# RESTRICCIONES: usar únicamente if, while, for (sin arreglos/listas, sin funciones, sin POO).

print('\033[H\033[J', end='')
print('--- Cuadrado Hueco con Carácter ---\n')

# --- Entrada de datos ---
lado = int(input("¿De qué tamaño será el lado del cuadrado? "))
car = input("¿Qué carácter quieres usar? ")

# Si el usuario no ingresa nada, usar un carácter por defecto ('#')
if car == "":
    car = "#"

# Tomar solo el primer carácter en caso de que el usuario escriba más de uno
car = car[0]

print()

# --- Dibujo del cuadrado hueco ---
# Recorremos filas (1..lado)
fila = 1
while fila <= lado:
    # Recorremos columnas (1..lado)
    col = 1
    while col <= lado:
        # En el contorno: primera/última fila o primera/última columna
        if fila == 1 or fila == lado or col == 1 or col == lado:
            # Imprimir el carácter y un espacio para dar separación uniforme
            print(car, end=" ")
        else:
            # Interior hueco: imprimir espacios de ancho equivalente
            print(" ", end=" ")
        col = col + 1
    # Fin de la fila actual: salto de línea
    print()
    fila = fila + 1
