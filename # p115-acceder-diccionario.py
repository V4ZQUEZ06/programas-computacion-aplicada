# p115-acceder-diccionario.py
# Acceder a elementos de un diccionario

print('\033[H\033[J')

# Crear diccionario
dias = {
    1 : 'Lunes',
    2 : 'Martes',
    3 : 'Miércoles',
    4 : 'Jueves',
    5 : 'Viernes',
    6 : 'Sábado',
    7 : 'Domingo'
}

print("Diccionario inicial:")
print(dias)

print("\nAccediendo a elementos:")

# Acceder usando []
print("Llave 1 (con []):", dias[1])
print("Llave 7 (con []):", dias[7])

# Acceder usando get()
print("Llave 5 (con get()):", dias.get(5))
print("Llave 7 (con get()):", dias.get(7))

print("\nDiccionario final:")
print(dias)
