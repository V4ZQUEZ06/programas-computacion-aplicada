# p074-suma-multiplos.py
# Imprime múltiplos de m entre 1 y n

while True:
    print('\033[H\033[J')

    print('Imprime múltiplos de m entre 1 y n')
    n = int(input('¿Hasta dónde? '))
    m = int(input('¿Qué múltiplos quieres? '))

    cm = sm = 0  # contador y suma de múltiplos

    for i in range(1, n + 1):
        if i % m == 0:
            print(i, end=' ')
            sm += i
            cm += 1

    print(f'\n\nFueron {cm} múltiplos, los cuales suman {sm}')

    if input('\n\n¿Deseas continuar (S/N)? ').upper() == 'N':
        break

print('\nHemos llegado al final...')
