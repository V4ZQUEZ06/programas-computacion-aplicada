# p055-tabla-multiplicar-while-v2.py
# Imprime todas las tablas de multiplicar desde la 1 hasta la n, desde el 1 hasta el m

while True:
    print('\033[H\033[J')  # Limpia pantalla
    print("Tablas de Multiplicar")

    # Validación de entradas
    while True:
        n = int(input("¿Hasta qué tabla quieres? "))
        m = int(input("¿Hasta dónde la quieres? "))
        if n > 0 and m > 0:
            break
        print("Error, los números deben ser mayores que 0")

    # Generar las tablas
    t = 1
    while t <= n:
        print(f"\nTabla del {t}\n")
        c = 1
        while c <= m:
            print(f"{t} x {c} = {t*c}")
            c += 1
        t += 1

    # Preguntar si continuar
    if input("\n\n¿Deseas Continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
