# p117-agregar-diccionario.py
# Agregar elementos a un diccionario

print('\033[H\033[J')

# Diccionario inicial
ventas = {
    'Juan': 1550,
    'Jose': 2600,
    'Maria': 2220
}

print("Ventas iniciales:")
print(ventas)

# Agregando nuevos vendedores
ventas['Rocio'] = 2500     # usando []
ventas['Mateo'] = 1567     # usando []
ventas.update({'Andrea': 9567})  # usando update()
ventas.update({'Miguel': 1234})  # usando update()

print("\nVentas actualizadas:")
print(ventas)
