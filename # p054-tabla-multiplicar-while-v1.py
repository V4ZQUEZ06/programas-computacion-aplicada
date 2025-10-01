# p054-tabla-multiplicar-while-v1.py
# Imprime la tabla de multiplicar deseada t, hasta el multiplo n

while True:
    print('\033[H\033[J')
    print("Imprime la tabla de multiplicar deseada t, hasta el múltiplo n")

    # Validación de entradas
    while True:
        t = int(input("¿Qué tabla quieres? "))
        n = int(input("¿Hasta dónde la quieres? "))
        if t > 0 and n > 0:
            break
        print("Error, los números deben ser mayores que 0")

    # Imprime la tabla
    c = 1
    while c <= n:
        print(f"{t} x {c} = {t*c}")
        c += 1

    # Preguntar si continuar
    if input("¿Deseas Continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
