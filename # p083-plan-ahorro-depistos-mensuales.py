# p083-plan-ahorro-depistos-mensuales.py
# Simula un plan de ahorro mensual con interés compuesto mensual.
# RESTRICCIONES: usar únicamente if, while, for (sin arreglos/listas, sin funciones, sin POO).

print('\033[H\033[J', end='')
print('--- Plan de Ahorro Detallado ---\n')

# --- Entrada de datos ---
monto_inicial = float(input("Monto inicial de ahorro: "))
deposito_mensual = float(input("Depósito mensual: "))
tasa_mensual_por = float(input("Tasa de interés mensual (%): "))
meses_totales = int(input("Número de meses a simular: "))

# --- Preparación de variables ---
# Convertir porcentaje a razón (ej. 1.5% -> 0.015)
tasa_mensual = tasa_mensual_por / 100.0

# Saldo de trabajo: inicia en el monto inicial
saldo = monto_inicial

# Acumuladores para el resumen
total_interes = 0.0
total_depositos = 0.0

print("\n--- Plan de Ahorro Detallado ---")

# --- Bucle principal por mes ---
mes = 1
while mes <= meses_totales:
    # Saldo inicial del mes actual (antes de intereses y depósito)
    saldo_inicial = saldo

    # Interés del mes calculado sobre el saldo inicial
    interes_mes = saldo_inicial * tasa_mensual

    # Saldo final después de sumar interés y depósito del mes
    saldo = saldo_inicial + interes_mes + deposito_mensual

    # Mostrar la fila del mes
    print(f"Mes {mes}: "
          f"Saldo Inicial: ${saldo_inicial:.2f} | "
          f"Interés: ${interes_mes:.2f} | "
          f"Saldo Final: ${saldo:.2f}")

    # Actualizar acumuladores
    total_interes = total_interes + interes_mes
    total_depositos = total_depositos + deposito_mensual

    # Avanzar al siguiente mes
    mes = mes + 1

# --- Resumen final ---
print("\n--- Resumen ---")
print(f"Saldo inicial: ${monto_inicial:.2f}")
print(f"Total depositado: ${total_depositos:.2f}")
print(f"Interés total ganado: ${total_interes:.2f}")
print(f"Saldo final: ${saldo:.2f}")
