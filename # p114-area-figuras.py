# p114-area-figuras.py
# Crear una lista de diccionarios para representar figuras geométricas

import math

figuras = {
    "Circulo":   {"radio": 0, "formula": "math.pi * r ** 2"},
    "Triangulo": {"base": 0, "altura": 0, "formula": "0.5 * b * a"},
    "Rectangulo":{"largo": 0, "ancho": 0, "formula": "l * a"}
}

print('\033[H\033[J')
print('Área de Figuras Geométricas\n')
print("Calculadora de áreas de figuras geométricas")
print("Figuras disponibles:")

for k, v in figuras.items():
    print(f'{k:<10} - Fórmula: {v["formula"]}')

while True:
    fig = input('\nElige una Figura: ').title()
    if fig in figuras:
        break
    print("Error: Figura no válida. Intenta de nuevo.")

area = 0

if fig == 'Circulo':
    r = float(input('Radio : '))
    area = eval(figuras[fig]['formula'].replace('r', str(r)))

elif fig == 'Triangulo':
    b = float(input('Base : '))
    a = float(input('Altura : '))
    formula = figuras[fig]['formula'].replace('b', str(b)).replace('a', str(a))
    area = eval(formula)

elif fig == 'Rectangulo':
    l = float(input('Largo : '))
    a = float(input('Ancho : '))
    formula = figuras[fig]['formula'].replace('l', str(l)).replace('a', str(a))
    area = eval(formula)

print(f'\nEl Área del {fig} es : {area:.4f}')
