# p026_convertir_temperaturas_v2.py
# Convierte temperaturas y ahora valida la opción del usuario.

print("\033[2J\033[H", end="")  # Borra la pantalla usando secuencias de escape ANSI
print("* Convierte entre Celsius y Fahrenheit *\n")

print("[C] para convertir a Celsius \n[F] para convertir a Fahrenheit")
op = input("Elige una opción: ").upper()

# Validación de la opción
if op == 'C':
    print("\nConvirtiendo a Celsius...")
    f = float(input("Introduce los grados Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print(f"\nResultado: {f:.2f}°F equivalen a {c:.2f}°C.")
elif op == 'F':
    print("\nConvirtiendo a Fahrenheit...")
    c = float(input("Introduce los grados Celsius: "))
    f = (c * 9 / 5) + 32
    print(f"\nResultado: {c:.2f}°C equivalen a {f:.2f}°F.")
else:
    print(f"\nOpción '{op}' no válida. Por favor, reinicia el programa y elige solo 'C' o 'F'.")

print("\n* ¡Programa finalizado! 😎 *")
