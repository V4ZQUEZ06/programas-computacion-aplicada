# p094-consolidar-ventas.py
# Consolidar las ventas de dos sucursales, usando listas

print('\033[H\033[J')
print('Consolidar ventas de dos sucursales\n')

# Leer número de elementos
elementos = int(input('¿Cuántas ventas diarias se registrarán? '))

# Inicializar listas
ventas_suc1 = []
ventas_suc2 = []
ventas_consolidadas = []

# Leer datos de la Sucursal 1
print('\nRegistrando ventas de la Sucursal 1:')
for i in range(elementos):
    venta = int(input(f'Venta del día {i + 1}: '))
    ventas_suc1.append(venta)

# Leer datos de la Sucursal 2
print('\nRegistrando ventas de la Sucursal 2:')
for i in range(elementos):
    venta = int(input(f'Venta del día {i + 1}: '))
    ventas_suc2.append(venta)

# Calcular la suma de ventas por día
for i in range(elementos):
    suma_dia = ventas_suc1[i] + ventas_suc2[i]
    ventas_consolidadas.append(suma_dia)

# Mostrar resultados
print('\n--- Reporte de Ventas ---')
print(f'Sucursal 1: {ventas_suc1}')
print(f'Sucursal 2: {ventas_suc2}')
print(f'Ventas Consolidadas: {ventas_consolidadas}')

# Estadísticas adicionales
print('\n--- Estadísticas Generales ---')
total_suc1 = sum(ventas_suc1)
total_suc2 = sum(ventas_suc2)
total_consolidado = sum(ventas_consolidadas)
print(f'Total Sucursal 1: {total_suc1}')
print(f'Total Sucursal 2: {total_suc2}')
print(f'Total Consolidado : {total_consolidado}')
print(f'Promedio diario (ambas sucursales): {total_consolidado / elementos:.2f}')
