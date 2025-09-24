# p043-calculadora-anio-bisiesto.py
# Determinar si un año es bisiesto o no.

print("--- Calculadora de Año Bisiesto ---")

# Entrada
anio = int(input("Dame un año: "))

# Verificación de condiciones
if (anio % 4 == 0 and anio % 100 != 0):
    print(f"El año {anio} es bisiesto. (Porque es divisible por 4 pero no por 100).")
elif (anio % 400 == 0):
    print(f"El año {anio} es bisiesto. (Porque es divisible por 400).")
else:
    print(f"El año {anio} no es bisiesto.", end=" ")

    # Explicación del porqué
    if anio % 100 == 0:
        print("(Porque es divisible por 100 pero no por 400).")
    elif anio % 4 != 0:
        print("(Porque no es divisible por 4).")
