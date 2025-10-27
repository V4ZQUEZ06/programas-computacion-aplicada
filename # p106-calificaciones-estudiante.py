# p106-calificaciones-estudiante.py
# Gestión de calificaciones de un estudiante usando diccionarios

print('\033[H\033[J')
print('Gestión de calificaciones de un estudiante usando diccionarios')

materias = ['Fisica', 'Quimica', 'Matematicas', 'Geografia', 'Estadistica']
califs = [10, 9, 8, 7.5, 6]

print(f'\nLista de materias : \n{materias}')
print(f'\nLista de calificaciones : \n{califs}')

# Crear diccionario uniendo listas
notas = dict(zip(materias, califs))
print(f'\nDiccionario nuevo juntando las dos listas:\n({len(notas)}) -> {notas}')

# Agregar materias nuevas
notas.update({'Ingles': 10})
notas.update({'Programacion': 7})
print(f'\nSe agregaron elementos:\n({len(notas)}) -> {notas}')

# Eliminar elementos
notas.pop('Fisica')
notas.popitem()  # elimina el último elemento agregado
print(f'\nSe removieron elementos:\n({len(notas)}) -> {notas}')

# Modificar elementos
notas.update({'Quimica': 10})
notas.update({'Matematicas': 10})
print(f'\nSe modificaron elementos:\n({len(notas)}) -> {notas}')

# Calcular promedio
suma = 0
print('\nMaterias y calificaciones finales')
for materia, cal in notas.items():
    print(f'{materia:<12} - {cal:>5}')
    suma += cal

prom = suma / len(notas)
print(f'\nLa suma: {suma} y el promedio: {prom:.2f}')

# Borrar todo
notas.clear()
print(f'\nSe borró todo : {notas}')
