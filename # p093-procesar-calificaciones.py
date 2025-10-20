# p093-procesar-calificaciones.py
# Procesa calificaciones en una lista

print('\033[H\033[J')
print('Procesador de calificaciones de un curso\n')
print("Introduce calificaciones entre 0 y 10 (usa 99 para terminar):\n")

calificaciones = []
suma = 0.0

while True:
    try:
        txt = input("Calificación > ").strip()
        # Permite Enter vacío sin romper
        if txt == "":
            print("Entrada vacía. Escribe un número (0–10) o 99 para terminar.")
            continue

        n = float(txt)

        if n == 99:
            break

        if 0.0 <= n <= 10.0:
            calificaciones.append(n)
            suma += n
        else:
            print("Error: la calificación debe estar entre 0 y 10.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")

if not calificaciones:
    print("\nNo se ingresaron calificaciones.")
else:
    promedio = suma / len(calificaciones)
    mayores_promedio = [c for c in calificaciones if c > promedio]

    print(f"\nSe capturaron {len(calificaciones)} calificaciones.")
    print(f"Las calificaciones son: {calificaciones}")

    print("\n--- Estadísticas del Curso ---")
    print(f"Suma total          : {suma:.2f}")
    print(f"Promedio            : {promedio:.2f}")
    print(f"Mayores al promedio : {len(mayores_promedio)} -> {mayores_promedio}")
    print(f"Calificación más alta: {max(calificaciones):.2f}")
    print(f"Calificación más baja: {min(calificaciones):.2f}")
