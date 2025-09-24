# p038-dia-semana.py
# Mostrar el día de la semana según un número del 1 al 7

print("--- Día de la Semana ---")

# Entrada del usuario
numero = int(input("Dame un número del 1 al 7: "))

# Diccionario para mapear número -> día
dias = {
    1: "Domingo",
    2: "Lunes",
    3: "Martes",
    4: "Miércoles",
    5: "Jueves",
    6: "Viernes",
    7: "Sábado"
}

# Verificación y salida
if numero in dias:
    print(dias[numero])
else:
    print("Error: Día inválido.")
