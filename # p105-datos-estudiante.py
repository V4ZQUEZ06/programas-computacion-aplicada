# p105-datos-estudiante.py
# Gestión de datos de estudiantes usando diccionarios

print('\033[H\033[J')
print('Gestión de datos de estudiantes')

estudiante = {
    'nombre': 'Juan Perez',
    'edad': 45,
    'email': 'jperez@msn.com',
    'carrera': 'Sistemas'
}

print(f'\nEl diccionario original:\n\n{estudiante}')

# Agregar y modificar datos
estudiante['calificacion'] = 9.5
estudiante['email'] = 'juanp@gmail.com'

print(f'\nEl diccionario actualizado:\n\n{estudiante}')

print('\nLas llaves del diccionario:\n')
for k in estudiante.keys():
    print(k)

print('\nLos valores del diccionario:\n')
for v in estudiante.values():
    print(v)

print("\nListado de llaves y valores:\n")
for k, v in estudiante.items():
    print(f'{k:<12} : {v}')
