# p032-aceptar-estudiante.py
# Aceptar a un estudiante en base a la edad y calificaciones.

print('--- Admisiones de la Universidad Patito ---')
nombre = input('Dame tu nombre: ')
edad = int(input('Dame tu edad: '))

# Primer nivel: verificar la edad
if edad < 18:
    print(f'Lo sentimos, {nombre}. Solo aceptamos a mayores de 18 años.')
else:
    # Si la edad es aceptable, pasar al siguiente nivel de verificación
    print('Ingresa 2 calificaciones para continuar:')
    calificacion1 = float(input('Calificación 1: '))
    calificacion2 = float(input('Calificación 2: '))

    # Segundo nivel: verificar las calificaciones
    if calificacion1 < 8 or calificacion2 < 8:
        print('Lo sentimos, se requiere una calificación mínima de 8 en ambos exámenes.')
    else:
        # Si ambas condiciones (edad y calificaciones) se cumplen
        print(f'¡Bienvenid@, {nombre}! Tu edad de {edad} y tus calificaciones te permiten ingresar.')
