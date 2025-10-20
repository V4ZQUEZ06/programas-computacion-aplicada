# p102-listas-aleatorios-suma.py
# Genera dos listas de números aleatorios y una tercera con la suma de impares

import random

print('\033[H\033[J')
print("=== Listas Aleatorias y Suma Condicional ===\n")

# ===== Generación de listas =====
lista_a = [random.randint(1, 20) for _ in range(10)]
lista_b = [random.randint(1, 20) for _ in range(10)]
lista_c = []

# ===== Procesamiento =====
for i in range(10):
    a = lista_a[i]
    b = lista_b[i]
    if a % 2 != 0 and b % 2 != 0:  # ambos impares
        lista_c.append(a + b)
    else:
        lista_c.append(0)

# ===== Resultados =====
print("--- Listas Generadas ---")
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")

print("\n--- Resultados (Suma solo si ambos son impares) ---")
print(f"Lista C: {lista_c}")

# ===== Explicación detallada (opcional) =====
print("\n--- Detalle del cálculo ---")
for i in range(10):
    cond = "✅ suma" if lista_c[i] != 0 else "❌ no cumple"
    print(f"A[{i}]={lista_a[i]:2}  B[{i}]={lista_b[i]:2}  →  C[{i}]={lista_c[i]:2}  ({cond})")
