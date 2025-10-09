# p082-compara-rendimiento-inversion.py
# Compara el crecimiento de dos fondos con interés compuesto anual.
# Restricciones: solo if, while, for (sin arreglos, sin funciones propias, sin POO).

print('\033[H\033[J', end='')
print("--- Comparador de Fondos de Inversión ---\n")

# --- Entrada de datos para el Fondo A ---
print("--- Fondo de Inversión A ---")
montoA = float(input("Monto inicial: "))
tasaA_por = float(input("Tasa de interés anual (%): "))

# --- Entrada de datos para el Fondo B ---
print("\n--- Fondo de Inversión B ---")
montoB = float(input("Monto inicial: "))
tasaB_por = float(input("Tasa de interés anual (%): "))

# --- Años a proyectar ---
anios = int(input("Años a proyectar: "))

# --- Conversión de porcentaje a razón (ej. 5% -> 0.05) ---
tasaA = tasaA_por / 100.0
tasaB = tasaB_por / 100.0

# --- Copias de trabajo para acumular el interés compuesto ---
saldoA = montoA
saldoB = montoB

# --- Encabezado de la tabla comparativa ---
print("\n--- Comparación de Rendimientos Anuales ---")
print("Año | Fondo A | Fondo B")
print("-------------------------------------------")

# --- Bucle principal (año por año) ---
i = 1
while i <= anios:
    # Interés compuesto anual: nuevo saldo = saldo * (1 + tasa)
    saldoA = saldoA * (1.0 + tasaA)
    saldoB = saldoB * (1.0 + tasaB)

    # Fila con formato a 2 decimales
    print(f"{i} | $ {saldoA:.2f} | $ {saldoB:.2f}")

    i = i + 1  # siguiente año

# --- Comparación final y mensaje de resultado ---
print("\nResultado final:", end=" ")
if saldoA > saldoB:
    print(f"El Fondo A (${'%0.2f' % saldoA}) superó al Fondo B (${'%0.2f' % saldoB}).")
elif saldoB > saldoA:
    print(f"El Fondo B (${'%0.2f' % saldoB}) superó al Fondo A (${'%0.2f' % saldoA}).")
else:
    print(f"Ambos fondos terminaron iguales: $ {'%0.2f' % saldoA}.")
