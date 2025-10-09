# p081-suma-potencias.py
# Calcula S = a^1 + a^2 + ... + a^n

print('\033[H\033[J', end='')
print('--- Suma de Potencias: S = a^1 + a^2 + ... + a^n ---\n')

# Leer n de forma segura (entero positivo)
while True:
    try:
        n = int(input("¿Hasta qué exponente n deseas sumar? (entero >= 1): "))
        if n < 1:
            print("Debes ingresar un entero positivo (>= 1).\n")
            continue
        break
    except ValueError:
        print("Entrada no válida. Escribe un entero.\n")

# Leer a de forma segura (permite enteros o reales)
while True:
    try:
        a = float(input("Ingresa la base a (puede ser real): "))
        break
    except ValueError:
        print("Entrada no válida. Escribe un número (ej. 2, -1.5, 0.5).\n")

print("\n--- Términos ---")
suma_iter = 0.0
potencia = 1.0  # iremos acumulando a^i multiplicando por 'a' cada vez

for i in range(1, n + 1):
    potencia *= a            # ahora potencia = a^i
    suma_iter += potencia
    # Mostrar término; formateo compacto para reales grandes o muy pequeños
    print(f"a^{i} = {potencia:.10g}")

print("\n--- Resultado por suma iterativa ---")
print(f"Suma iterativa: {suma_iter:.12g}")

# Cálculo con fórmula geométrica cuando es válido (a != 1)
EPS = 1e-12
if abs(a - 1.0) < EPS:
    suma_formula = float(n)  # si a == 1, S = 1 + 1 + ... + 1 = n
    print("Fórmula (caso a = 1): S = n")
    print(f"Suma por fórmula: {suma_formula:.12g}")
else:
    # S = a + a^2 + ... + a^n = (a^(n+1) - a) / (a - 1)
    try:
        suma_formula = (a ** (n + 1) - a) / (a - 1)
        print("Fórmula geométrica: S = (a^(n+1) - a) / (a - 1)")
        print(f"Suma por fórmula: {suma_formula:.12g}")
        # Comparación (puede diferir por redondeo en floats)
        diff = abs(suma_iter - suma_formula)
        print(f"Diferencia |iter - fórmula| = {diff:.3e}")
    except OverflowError:
        print("Advertencia: la potencia a^(n+1) desbordó (Overflow).")
        print("No se muestra el resultado por fórmula en este caso.")
