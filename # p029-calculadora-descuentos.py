# p029-calculadora-descuentos.py
# Simula una calculadora de descuentos basada en el monto de la compra

print("Calculadora de Descuentos 💰 \n")

compra = float(input("Ingresa el total de tu compra: $"))

# Definimos las variables para el descuento
descuento = 0
porcentaje = 0

if compra > 2000:
    porcentaje = 0.20  # 20% de descuento
    descuento = compra * porcentaje
elif compra > 1000:
    porcentaje = 0.10  # 10% de descuento
    descuento = compra * porcentaje
elif compra > 500:
    porcentaje = 0.05  # 5% de descuento
    descuento = compra * porcentaje
else:
    # Si no aplica ninguno de los descuentos anteriores
    descuento = 0

# Calculamos y mostramos el resultado
total = compra - descuento

print(f"\nMonto de la compra : ${compra:,.2f}")
print(f"Descuento aplicado : {porcentaje*100:.0f}%")
print(f"Total a pagar      : ${total:,.2f}")
