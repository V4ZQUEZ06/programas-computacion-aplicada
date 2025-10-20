# p099-procesar-notas.py
# Procesar notas (calificaciones) y generar estadísticas

print('\033[H\033[J')
print("=== Procesador de Notas ===\n")
print("Introduce notas entre 0 y 100 (usa 0 para detener)\n")

notas = []

# ===== Captura de datos =====
while True:
    try:
        n = float(input("Introduzca nota (0 para detener): "))
        if n == 0:
            break
        if 0 < n <= 100:
            notas.append(n)
        else:
            print("⚠️  Entrada inválida: la nota debe estar entre 0 y 100.")
    except ValueError:
        print("❌ Error: introduce un número válido.")

# ===== Procesamiento =====
if not notas:
    print("\nNo se introdujeron notas.")
else:
    total_notas = len(notas)
    suma_notas = sum(notas)
    promedio = suma_notas / total_notas
    nota_max = max(notas)
    nota_min = min(notas)
    menores_promedio = [n for n in notas if n < promedio]

    # ===== Resultados =====
    print("\n--- Resultados ---")
    print(f"Total de notas introducidas: {total_notas}")
    print(f"Lista de notas: {notas}")
    print(f"Suma de notas: {suma_notas:.2f}")
    print(f"Promedio de notas: {promedio:.2f}")
    print(f"Nota máxima: {nota_max}")
    print(f"Nota mínima: {nota_min}")
    print(f"Notas menores al promedio ({promedio:.2f}): {len(menores_promedio)}")
    print(f"Lista de notas menores al promedio: {menores_promedio}")
