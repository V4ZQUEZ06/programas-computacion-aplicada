# p004-paga-trabajador.py
# Calcular la paga total de un trabajador

print('Calculando la paga de un trabajador')
print('Nombre : ')
nombre = input()
print('Horas trabajadas : ')
horas = int(input())
print('Paga por hora : ')
paga = float(input())

tasa = 0.3
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print('Resumen de pagos:\n')
print(f'El trabajador {nombre}, trabajo {horas} horas, con una paga de {paga} pesos por hora, impuesto de {tasa}%')
print(f'Paga bruta {pagabruta}')
print(f'Impuesto {impuesto}')
print(f'Paga neta {paganeta}')