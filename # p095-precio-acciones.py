# p095-precio-acciones.py
# Análisis básico de portafolio de acciones

print('\033[H\033[J')
print("Análisis de precios semanales de una acción\n")

# ===== Datos =====
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
precios = [150.25, 152.50, 149.75, 155.00, 153.20]

# ===== Cálculos =====
precio_max = max(precios)
precio_min = min(precios)
pos_max = precios.index(precio_max)
pos_min = precios.index(precio_min)
promedio = sum(precios) / len(precios)
variacion = precio_max - precio_min

# ===== Resultados =====
print("Precios de cierre:")
for d, p in zip(dias, precios):
    print(f"  {d:<10} → ${p:.2f}")

print("\n--- Resumen Semanal ---")
print(f"Precio más alto : ${precio_max:.2f} ({dias[pos_max]})")
print(f"Precio más bajo  : ${precio_min:.2f} ({dias[pos_min]})")
print(f"Promedio semanal : ${promedio:.2f}")
print(f"Variación total  : ${variacion:.2f}")
print(f"Diferencia porcentual: {((variacion / precio_min) * 100):.2f}%")
