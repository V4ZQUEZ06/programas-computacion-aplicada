# p040-calculo-notas.py
# Calcular el promedio de 5 calificaciones y mostrar un mensaje según el resultado.

print("--- Cálculo de Promedio de 5 Calificaciones ---")

# Entrada de 5 calificaciones
c1 = float(input("Dame la primera calificación: "))
c2 = float(input("Dame la segunda calificación: "))
c3 = float(input("Dame la tercera calificación: "))
c4 = float(input("Dame la cuarta calificación: "))
c5 = float(input("Dame la quinta calificación: "))

# Calcular promedio
promedio = (c1 + c2 + c3 + c4 + c5) / 5

# Mostrar el promedio
print(f"Tu promedio es {promedio:.1f}.", end=" ")

# Evaluar mensaje según rango
if promedio < 6:
    print("Quedas reprobado")
elif promedio < 7:
    print("Pasas de panzazo")
elif promedio < 8:
    print("Muy bien, puedes mejorar")
elif promedio < 9:
    print("Excelente, sigue así")
elif promedio <= 10:
    print("Perfecto, tu esfuerzo valió la pena")
else:
    print("Error: Promedio fuera de rango")
