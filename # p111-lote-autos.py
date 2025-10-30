# p111-lote-autos.py
# Crear una lista de diccionarios para representar un lote de autos

autos = [
    { 'marca':'Ford', 'modelo':'Mustang', 'año': 1964 },
    { 'marca':'VW', 'modelo':'Jetta', 'año': 2015 }
]
autos.append({ 'marca':'Ford', 'modelo':'Focus', 'año': 2000 })

print('\033[H\033[J')
print('='*50)
print('Listado de Autos')
print('='*50)

print(f'\nTodos los autos : {autos} \nTotal: {len(autos)}')

print('\nCada auto dentro de los autos:')
print('-'*50)
for auto in autos:
    print(auto)

print('\nDatos en forma de Tabla:')
print('-'*50)

# Encabezados
for k in autos[0].keys():
    print(f'{k}\t', end='')
print('\r')

# Valores
for auto in autos:
    for v in auto.values():
        print(f'{v}\t', end='')
    print('\r')

print('\nDatos en forma de Registro')
print('-'*50)
for auto in autos:
    for k, v in auto.items():
        print(f'{k:<12} : {v}')
    print('')
