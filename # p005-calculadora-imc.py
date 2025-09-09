# p005-calculadora-imc.py
# Calcular el IMC de una person


print("Calculadora de Índice de Masa Corporal (IMC):\n")
peso_kg = float(input("Ingresa tu peso en kilogramos: "))
altura_m = float(input("Ingresa tu altura en metros: "))
imc = peso_kg / (altura_m ** 2)
print(f"Tu IMC es: {imc:.2f}")