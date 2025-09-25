# p049-sumar-consecutivos.py
# Suma números hasta que el total sea >= 100.

c = 0
suma = 0
print("Meta de ahorro: $100. Empezando a sumar números...")

# El ciclo está programado para correr hasta 200, pero el 'break' lo detendrá antes.
while c < 200:
    c += 1
    suma += c
    print(f" (+{c})", end="")

    # Verificamos si hemos alcanzado o superado la meta.
    if suma >= 100:
        print("\n\n¡Meta alcanzada!")
        # La palabra 'break' termina el ciclo INMEDIATAMENTE.
        break

# Este mensaje se imprime después de que el ciclo ha terminado (por 'break' o de forma natural).
print(f"Se necesitaron los primeros {c} números para llegar a una suma de ${suma}.")
