# p103-ciudades.py
# Registro y análisis de nombres de ciudades

print('\033[H\033[J')
print("=== Registro de Ciudades ===\n")
print("Introduce nombres de ciudades (usa '$' para detener)\n")

# ===== Captura de datos =====
ciudades = []

while True:
    nombre = input("Introduzca nombre de ciudad ($ para detener): ").strip()
    if nombre == "$":
        break
    if nombre == "":
        print("⚠️  El nombre no puede estar vacío.")
        continue
    ciudades.append(nombre)

# ===== Procesamiento =====
if not ciudades:
    print("\nNo se introdujeron ciudades.")
else:
    # Lista ordenada descendente
    ciudades_desc = sorted(ciudades, reverse=True)

    # Detección de consonantes
    vocales = ['A', 'E', 'I', 'O', 'U']
    ciudades_consonante = [
        c for c in ciudades if c[0].upper() not in vocales
    ]

    # ===== Resultados =====
    print("\n--- Resultados ---")
    print(f"Total de ciudades introducidas: {len(ciudades)}")
    print(f"Lista original: {ciudades}")
    print(f"Lista ordenada descendente: {ciudades_desc}")
    print(f"Ciudades que inician con consonante: {len(ciudades_consonante)}")
    print(f"Lista de ciudades con consonante inicial: {ciudades_consonante}")
