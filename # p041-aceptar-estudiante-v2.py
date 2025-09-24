# p041-aceptar-estudiante-v2.py
# Universidad Kitty Kat SA - Evaluación de aspirantes

print("--- Admisiones Universidad Kitty Kat SA ---")

# Entradas
nombre = input("Dame tu nombre: ")
sexo = input("Dame tu sexo (h/m): ").lower()  # Convertimos a minúsculas
edad = int(input("Dame tu edad: "))

print("Ingresa tres calificaciones:")
c1 = float(input("Calificación 1: "))
c2 = float(input("Calificación 2: "))
c3 = float(input("Calificación 3: "))

# Cálculo del promedio
promedio = (c1 + c2 + c3) / 3

# Evaluación de requisitos
if sexo != "m":
    print(f"Lo sentimos, {nombre}. La universidad solo acepta mujeres.")
elif edad <= 21:
    print(f"Lo sentimos, {nombre}. No cumples con la edad requerida (mayores de 21 años).")
elif promedio < 8:
    print(f"Lo sentimos, {nombre}. Tu promedio de {promedio:.2f} no alcanza el mínimo requerido de 8.")
elif promedio > 9.5:
    print(f"Lo sentimos, {nombre}. Tu promedio de {promedio:.2f} excede el máximo permitido de 9.5.")
else:
    print(f"¡Felicidades, {nombre}! Has sido aceptada. Cumples con la edad y tu promedio de {promedio:.2f} está dentro del rango permitido.")
