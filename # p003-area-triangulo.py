# p003-area-triangulo.py
# Calcula el area de un triangulo

print('Calculando el area de un triangulo \n')

# Entrada
print('Dame la base y la altura separados por Enter')
base, altura = int(input()), int(input())  # lee dos valores

# Proceso
area = ( base * altura ) / 2

# Salida
print('El triangulo de base ', base)
print('El triangulo de altura ', altura)
print('Tiene un area de ', area)
