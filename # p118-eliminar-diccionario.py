# p118-eliminar-diccionario.py
# Eliminar elementos de un diccionario

print('\033[H\033[J')

# Diccionario inicial
municipios = {
    'Apozol': 1863,
    'Calera': 1868,
    'Fresnillo': 1554,
    'Guadalupe': 1821,
    'Jalpa': 1824,
    'Jerez': 1824,
    'Loreto': 1931,
    'Mazapil': 1824,
    'Momax': 1857
}

print("Diccionario inicial:")
print(municipios)

# Eliminar Apozol usando del
del municipios['Apozol']
print("\nDespués de 'del Apozol':")
print(municipios)

# Eliminar Fresnillo usando pop()
municipios.pop('Fresnillo')
print("\nDespués de 'pop(\"Fresnillo\")':")
print(municipios)

# Eliminar el último elemento usando popitem()
municipios.popitem()  # elimina Momax
print("\nDespués de 'popitem()' (eliminando Momax):")
print(municipios)

# Vaciar el diccionario con clear()
municipios.clear()
print("\nDespués de 'clear()':")
print(municipios)
