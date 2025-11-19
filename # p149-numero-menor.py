# p149-numero-menor.py
# Función que solicita 3 números enteros al usuario y devuelve el menor

def numero_menor() -> int:
    print("Introduce tres números enteros.")
    
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
    n3 = int(input("Introduce el tercer número: "))

    menor = n1  # Suponemos que el primero es el menor

    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3

    return menor

# Ejemplo de uso
resultado = numero_menor()
print(f"El número menor es: {resultado}")
