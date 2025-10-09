# p085-rombo-caracter.py
# Dibuja un rombo (diamante) con un número impar de altura/ancho máximo.
# RESTRICCIONES: usar únicamente if, while, for (sin arreglos/listas, sin funciones, sin POO).

print('\033[H\033[J', end='')
print('--- Rombo con Carácter ---\n')

# --- Lectura y validación de la altura (n debe ser impar y >= 1) ---
while True:
    try:
        n = int(input("Dame un número impar para la altura: "))
        if n >= 1 and (n % 2 == 1):
            break
        else:
            print("Debes ingresar un entero impar (>= 1).\n")
    except ValueError:
        print("Entrada no válida. Escribe un entero.\n")

# --- Lectura del carácter a usar ---
car = input("¿Qué carácter quieres usar? ")
if car == "":
    car = "*"
else:
    car = car[0]  # usar solo el primer carácter

print("\n--- Rombo generado ---")

# Cambia a 0 si prefieres el estilo del ejemplo (alineado a la izquierda, sin espacios delante)
alinear_centro = 1  # 1 = centrado (rombo clásico), 0 = sin espacios (como en el ejemplo dado)

# -----------------------------
# PARTE SUPERIOR (incluye la fila central)
# Empieza con 1, luego 3, 5, ..., hasta n caracteres
# -----------------------------
anchura = 1
while anchura <= n:
    # Si se elige centrado, imprimir espacios a la izquierda
    if alinear_centro == 1:
        espacios = (n - anchura) // 2
        c = 1
        while c <= espacios:
            print(" ", end="")
            c = c + 1

    # Imprimir los caracteres de la fila
    k = 1
    while k <= anchura:
        print(car, end="")
        k = k + 1

    # Salto de línea y avanzar a la siguiente anchura (de 2 en 2)
    print()
    anchura = anchura + 2

# -----------------------------
# PARTE INFERIOR (sin la fila central)
# Baja con n-2, n-4, ..., hasta 1
# -----------------------------
anchura = n - 2
while anchura >= 1:
    if alinear_centro == 1:
        espacios = (n - anchura) // 2
        c = 1
        while c <= espacios:
            print(" ", end="")
            c = c + 1

    k = 1
    while k <= anchura:
        print(car, end="")
        k = k + 1

    print()
    anchura = anchura - 2
