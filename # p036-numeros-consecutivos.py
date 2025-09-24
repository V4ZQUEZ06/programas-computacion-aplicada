# p036-numeros-consecutivos.py
# Determinar si tres números enteros son consecutivos.

print("--- Verificador de Números Consecutivos ---")

# Entrada de tres números enteros
n1 = int(input("Dame el primer número: "))
n2 = int(input("Dame el segundo número: "))
n3 = int(input("Dame el tercer número: "))

# Ordenamos los números para simplificar la verificación
numeros = sorted([n1, n2, n3])

# Verificamos si son consecutivos
if numeros[1] - numeros[0] == 1 and numeros[2] - numeros[1] == 1:
    print("Los números son consecutivos.")
else:
    print("Los números no son consecutivos.")
