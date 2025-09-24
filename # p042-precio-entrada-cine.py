# p042-precio-entrada-cine.py
# Determinar el precio de la entrada al cine según la edad del cliente.

print("--- Taquilla del Cine ---")

# Entrada de edad
edad = int(input("Dame tu edad: "))

# Evaluar precio según rango de edad
if edad < 5:
    print("Tu entrada es gratis.")
elif edad <= 12:
    print("El precio de tu entrada es de $5.")
elif edad <= 64:
    print("El precio de tu entrada es de $10.")
else:  # 65 o más
    print("El precio de tu entrada es de $7.")
