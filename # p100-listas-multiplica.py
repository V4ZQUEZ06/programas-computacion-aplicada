# p100-listas-multiplica.py
# Multiplica los elementos correspondientes de dos listas

print('\033[H\033[J')
print("=== Multiplicación de Listas ===\n")

# ===== Entrada de datos =====
try:
    lista_a = list(map(float, input("Introduzca 5 números para la Lista A (separados por espacio): ").split()))
    lista_b = list(map(float, input("Introduzca 5 números para la Lista B (separados por espacio): ").split()))

    # Validar que ambas listas tengan 5 elementos
    if len(lista_a) != 5 or len(lista_b) != 5:
        print("\n❌ Error: cada lista debe contener exactamente 5 elementos.")
    else:
        # ===== Procesamiento =====
        lista_c = []
        for i in range(5):
            lista_c.append(lista_a[i] * lista_b[i])

        # ===== Resultados =====
        print("\n--- Resultados ---")
        print(f"Lista A: {lista_a}")
        print(f"Lista B: {lista_b}")
        print(f"Lista C (A * B): {lista_c}")

except ValueError:
    print("\n❌ Error: introduce solo números válidos separados por espacios.")
