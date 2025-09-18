# p027-calcular-paga-extra.py
# Calcula la paga de un trabajador considerando horas extra.

print("\033[2J\033[H", end="")  # Borra pantalla
print('Calculando la paga de un trabajador ')

# --- Entrada de datos ---
print("Datos del trabajador: \n")
nombre = input('Nombre del trabajador 👨‍🦱 : ')
horas = int(input('Horas trabajadas ⏲️: '))
paga_hora = float(input('Paga por hora 💰: '))

# --- Cálculo de la paga ---
horas_normales = 40
paga_normal = horas_normales * paga_hora
horas_extra = paga_extra = 0

if horas > 40:
    horas_extra = horas - 40
    paga_extra = horas_extra * (paga_hora * 2)
    total = paga_normal + paga_extra
else:
    total = paga_normal

# --- Salida ---
print("\nCálculo completado.")
print(f'\nEl trabajador {nombre} tiene {horas_normales} horas normales + {horas_extra} horas extra.')
print(f'Paga normal = ${paga_normal:13,.2f}')
print(f'Paga extra  = ${paga_extra:13,.2f}')
print(f'El pago total = ${total:13,.2f}')
print('\n* ¡Programa finalizado! 🔚 *')
