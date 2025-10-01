# p062-conversion-temperaturas.py
# Convierte un rango de temperaturas de °C a °F

while True:
    print('\033[H\033[J')  # Limpia pantalla
    print("Conversión de Temperaturas (°C a °F)\n")

    # Entradas validadas
    while True:
        t_inicial = int(input("Introduce la temperatura inicial en °C: "))
        t_final = int(input("Introduce la temperatura final en °C: "))
        if t_final >= t_inicial:
            break
        print("Error: La temperatura final debe ser mayor o igual a la inicial.")

    # Mostrar tabla
    print("-" * 20)
    c = t_inicial
    while c <= t_final:
        f = (c * 9/5) + 32
        print(f"{c}°C = {f:.1f}°F")
        c += 1

    # Preguntar si continuar
    if input("\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\nFin del programa. ¡Gracias!")
