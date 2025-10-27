# p107-nombres-edades.py
# Gestión de nombres y edades usando diccionarios

print('\033[H\033[J')
print('Gestión de nombres y edades usando diccionarios\n')

datos = {}
print('Introduce nombres y edades (nombre vacío para terminar)\n')

while True:
    nombre = input('Dame el nombre: ')
    if nombre == '':
        break
    else:
        datos[nombre] = int(input('Edad: '))

print(f'\nEl diccionario de datos creado:\n({len(datos)}) -> {datos}\n')

print('\nListado y promedio de edades:\n')
suma = 0
for n, e in datos.items():
    print(f'{n:<20} - {e:2}')
    suma += e

prom = suma / len(datos)
print(f'\nSuma: {suma} y Promedio: {prom:.2f}')
