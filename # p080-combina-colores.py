# p080-combina-colores.py
# Genera combinaciones de dos colores a partir de una lista

print('\033[H\033[J', end='')
print("--- Generador de Combinaciones de Colores ---\n")

# Leer y normalizar entrada
entrada = input("Ingresa los colores separados por comas: ")
tokens = [c.strip() for c in entrada.split(',')]
tokens = [c for c in tokens if c]  # quitar vacíos

# Eliminar duplicados preservando el orden (comparación insensible a mayúsculas)
colores = []
visto = set()
for c in tokens:
    k = c.casefold()
    if k not in visto:
        visto.add(k)
        colores.append(c)

if len(colores) < 2:
    print("\nNecesitas al menos 2 colores distintos.")
    print(f"Detecté: {colores}")
else:
    print(f"\nColores base ({len(colores)}): {', '.join(colores)}")
    print("\n--- Combinaciones (sin repetir orden) ---")
    total = 0
    for i in range(len(colores)):
        for j in range(i + 1, len(colores)):
            print(f"- {colores[i]} y {colores[j]}")
            total += 1
    print(f"\nTotal: {total} combinación(es).")
