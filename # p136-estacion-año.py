# p136-estacion-año.py
# Dado un número, regresar una cadena con el nombre de la estación del año.

def estacion_ano(mes: int) -> str:
    if mes in [12, 1, 2]:
        return "Invierno"
    elif mes in [3, 4, 5]:
        return "Primavera"
    elif mes in [6, 7, 8]:
        return "Verano"
    elif mes in [9, 10, 11]:
        return "Otoño"
    else:
        return "Mes inválido"

print('Dame un número de mes (1-12):')
mes = int(input())
print(f'La estación del año para el mes {mes} es: {estacion_ano(mes)}')

# Ejemplo de uso:
print(f'El mes 1 corresponde a: {estacion_ano(1)}')
print(f'El mes 4 corresponde a: {estacion_ano(4)}')
print(f'El mes 7 corresponde a: {estacion_ano(7)}')
