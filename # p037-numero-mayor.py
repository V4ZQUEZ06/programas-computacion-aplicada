# p037-numero-mayor.py
# Identificar el mayor de tres números enteros

print("--- Número Mayor ---")

# Entrada de datos
n1 = int(input("Dame el primer número: "))
n2 = int(input("Dame el segundo número: "))
n3 = int(input("Dame el tercer número: "))

# Uso de la función max()
mayor = max(n1, n2, n3)

print(f"El número mayor es {mayor}.")
