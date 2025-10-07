# p073-suma-promedio-numeros.py
# Suma de n números introducidos por el usuario usando ciclo for

while True:
    print('\033[H\033[J')
    cuantos = int(input('¿Cuántos números deseas procesar? '))
    suma = 0
    cadnum = ""

    for i in range(1, cuantos + 1):
        n = int(input(f'Número[{i}] = '))
        suma += n
        cadnum = cadnum + ' ' + str(n)

    print(f'\nLos números que introdujiste fueron:{cadnum}')
    print(f'La suma es {suma}, el promedio es {suma / cuantos:.2f}')

    if input('\n\n¿Deseas continuar (S/N)? ').upper() == 'N':
        break

print('\nHemos llegado al final...')
