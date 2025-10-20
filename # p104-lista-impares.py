# p104-lista-impares.py
# Genera una lista con los primeros n números impares y realiza análisis

print('\033[H\033[J')
print("=== Análisis de Números Impares ===\n")

try:
    n = int(input("Introduzca la cantidad de números impares (n): "))
    if n <= 0:
        print("❌ Error: debe introducir un número entero positivo.")
    else:
        # --- Generación de lista ---
        impares = [2*i + 1 for i in range(n)]
        print("\n--- Generación de Lista ---")
        print(f"Lista de los primeros {n} números impares: {impares}")

        # --- Cálculos ---
        suma_total = sum(impares)
        promedio = suma_total / len(impares)
        print("\n--- Cálculos ---")
        print(f"Suma de los números: {suma_total}")
        print(f"Promedio de los números: {promedio:.2f}")

        # --- Divisibles entre 3 ---
        divisibles_3 = [x for x in impares if x % 3 == 0]
        suma_div3 = sum(divisibles_3)
        print("\n--- Divisibles entre 3 ---")
        print(f"Números divisibles entre 3: {divisibles_3}")
        print(f"Suma de los números divisibles entre 3: {suma_div3}")

        # --- Búsqueda ---
        print("\n--- Búsqueda ---")
        try:
            elemento = int(input("Introduzca elemento a buscar: "))
            if elemento in impares:
                indice = impares.index(elemento)
                print(f"✅ El elemento {elemento} está en la lista en la posición (índice) {indice}.")
            else:
                print(f"❌ El elemento {elemento} no está en la lista.")
        except ValueError:
            print("❌ Entrada inválida. Debe ser un número entero.")

except ValueError:
    print("❌ Error: entrada inválida. Debe ser un número entero.")
