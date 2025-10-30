# p112-registro-estudiantes.py
# Crear una lista de diccionarios para representar un registro de estudiantes

grupo = [
    {'nombre':'Carlos','edad':45,'carrera':'sistemas','promedio':9},
    {'nombre':'Rocio','edad':35,'carrera':'sistemas','promedio':10}
]

print('\033[H\033[J')
print('Registro de Estudiantes\n')

print('\nGrupo de estudiantes inicial:')
print('-' * 60)
print(f'{grupo} - {len(grupo)}')

print('\nCaptura de nuevos estudiantes')
print('-' * 60)

while True:
    print('Datos Estudiante:')
    datos = {}
    nombre = input('Nombre ? ')
    
    if nombre != '':
        datos['nombre'] = nombre
        datos['edad'] = int(input('Edad? '))
        datos['carrera'] = input('Carrera ? ')
        datos['promedio'] = float(input('Promedio? '))
        grupo.append(datos)
    else:
        break

print('\nGrupo de estudiantes completo:')
print('-' * 60)
print(f'{grupo} - {len(grupo)}')

print('\nDatos en forma de Tabla:')
print('-' * 60)

# Encabezados
for k in grupo[0].keys():
    print(f'{k:<13}', end='')
print()

# Valores
for alumno in grupo:
    for v in alumno.values():
        print(f'{v:<13}', end='')
    print()

print('\nDatos en forma de Registro y Cálculo de Promedios:')
print('-' * 60)

s = 0
for est in grupo:
    s += est['promedio']
    for k, v in est.items():
        print(f'{k:<10} : {v}')
    print()

print('\nCálculo de Promedios:')
print('-' * 60)
p = s / len(grupo)
print(f'La suma es {s}')
print(f'El promedio es {p:.2f}')
