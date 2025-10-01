# p057-interes-simple.py
# Calcula los años necesarios para alcanzar una meta de ahorro con interés simple.

while True:
    print('\033[H\033[J')
    print("Calculadora de Años para Meta de Ahorro (Interés Simple)")
    print("-" * 60)

    # Validación de entradas
    while True:
        capital_inicial = float(input("Introduce el capital inicial: "))
        tasa_interes = float(input("Introduce la tasa de interés anual (%): "))
        meta_ahorro = float(input("Introduce la meta de ahorro: "))

        if capital_inicial > 0 and tasa_interes > 0 and meta_ahorro > capital_inicial:
            break
        else:
            print("Error: Asegúrate de que los valores sean positivos y la meta sea mayor al capital inicial.")

    # Cálculo con interés simple
    capital_actual = capital_inicial
    anios = 0
    interes_anual_fijo = capital_inicial * (tasa_interes / 100)

    while capital_actual <= meta_ahorro:
        capital_actual += interes_anual_fijo
        anios += 1

    # Resultados
    print("\n" + "-" * 60)
    print(f"Para alcanzar o superar tu meta de ${meta_ahorro:,.2f}, necesitarás {anios} años.")
    print(f"El monto final acumulado será de ${capital_actual:,.2f}.")
    print("-" * 60)

    # Preguntar si continuar
    res = input("\n¿Deseas realizar otro cálculo (S/N)? ").upper()
    if res == "N":
        break

print("\nFin del programa. ¡Éxito con tus ahorros!")
