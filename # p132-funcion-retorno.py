# p132-funcion-retorno.py

def suma(n1: float, n2: float) -> float:
    return n1 + n2

print('\nSuma de dos numeros constantes: ')
# Se guarda el valor retornado por la función
suma_resultado = suma(10, 20)
print(f"La suma es {suma_resultado}")

print('\nDame dos numeros separados por enter: ')
a, b = int(input()), int(input())
# Se imprime directamente el valor retornado por la función
print(f"La suma de los numeros es {suma(a, b)}")
