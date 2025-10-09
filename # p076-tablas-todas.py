# p076-tablas-todas.py
# Imprime las tablas de multiplicar de 1 a n, hasta m

print('\033[H\033[J', end='')  # limpia pantalla (ANSI)

# --- Lectura segura de n y m ---
while True:
    try:
        n = int(input("¿Hasta qué tabla de multiplicar deseas generar? "))
        m = int(input("¿Hasta qué número deseas multiplicar cada tabla? "))
        if n <= 0 or m <= 0:
            print("Por favor, ingresa enteros positivos (mayores que 0).\n")
            continue
        break
    except ValueError:
        print("Entrada no válida. Escribe números enteros.\n")

print("\n--- Generando Tablas de Multiplicar ---")

# Anchos para alinear columnas de forma dinámica
iw = len(str(n))         # ancho para i
jw = len(str(m))         # ancho para j
rw = len(str(n * m))     # ancho para el resultado

# Bucle exterior: itera por cada tabla (1, 2, 3, ... n)
for i in range(1, n + 1):
    print(f"\n--- Tabla del {i} ---")
    # Bucle interior: multiplicadores (1, 2, ... m)
    for j in range(1, m + 1):
        resultado = i * j  # ojo: aquí es i * j (correcto)
        print(f"{i:>{iw}} x {j:>{jw}} = {resultado:>{rw}}")
