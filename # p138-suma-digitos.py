# p138-suma-digitos.py
# Dado un número entero, sumar sus dígitos individuales

def suma_digitos(numero: int) -> int:
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma

def main() -> None:
    numero = int(input("Introduce un número entero: "))
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es {resultado}")

if __name__ == "__main__":
    main()
