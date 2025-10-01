# p052-tabla-conversion.py
# Muestra una tabla de conversión de Pesos a Dólares

tc = 20.71  # Tipo de cambio

while True:
    print('\033[H\033[J')  # Limpia pantalla en terminal compatible
    print("Tabla de Conversión Peso a Dollar")
    print(f"Tipo de Cambio: {tc} Pesos por Dollar")
    print("-" * 30)

    # Validación de valores inicial y final
    while True:
        pi = float(input("Valor inicial: "))
        pf = float(input("Valor final  : "))

        if (pi > 0 and pf > 0) and (pi < pf):
            break
        print("Error en los valores, intente de nuevo")

    # Imprime tabla
    print("\nPesos\tDollar")
    print("-" * 30)
    c = pi
    while c <= pf:
        print(f"{c:.2f}\t{c/tc:.2f}")
        c += 1
    print("-" * 30)

    # Continuar o salir
    res = input("¿Deseas continuar (S/N)? ").upper()
    if res == "N":
        break
