# p047-conteo-descendente-v2.py
# Imprime los números de n a 1, en decrementos de m, usando un ciclo while

print("Iniciando cuenta regresiva...")
n = int(input("¿Desde dónde? "))
m = int(input("¿De cuánto en cuánto? "))

c = n
while c >= 1:
    print(f"{c} ", end="")
    c -= m

print("\n¡Despegue!")
