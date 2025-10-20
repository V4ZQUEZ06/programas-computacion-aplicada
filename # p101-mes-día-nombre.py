# p101-mes-día-nombre.py
# Muestra el nombre del mes y su número de días

print('\033[H\033[J')
print("=== Consulta de Mes y Días ===\n")

# ===== Listas predefinidas =====
nombres_meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]
dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# ===== Entrada del usuario =====
try:
    numero_mes = int(input("Introduzca un número de mes (1-12): "))

    if 1 <= numero_mes <= 12:
        nombre = nombres_meses[numero_mes - 1]
        dias = dias_mes[numero_mes - 1]

        print("\n--- Resultados ---")
        print(f"Mes : {nombre}")
        print(f"Días: {dias}")
    else:
        print("\n❌ Error: el número de mes debe estar entre 1 y 12.")

except ValueError:
    print("\n❌ Error: debe introducir un número entero válido.")
