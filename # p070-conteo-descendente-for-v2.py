# p070-conteo-descendente-for-v2.py
# Imprime los números de n a 1, en decrementos de m, usando un ciclo for

print("Iniciando cuenta regresiva...")

n = int(input("¿Desde dónde? "))
m = int(input("¿De cuánto en cuánto? "))

for x in range(n, 0, -m):
    print(x, end=' ')
