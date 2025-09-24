# p039-numeros-romanos.py
# Convertir un número del 1 al 10 a números romanos

print("--- Conversor a Números Romanos ---")

# Entrada
numero = int(input("Dame un número entre 1 y 10: "))

# Diccionario de equivalencias
romanos = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X"
}

# Verificación y salida
if numero in romanos:
    print(romanos[numero])
else:
    print("Error: Número inválido.")