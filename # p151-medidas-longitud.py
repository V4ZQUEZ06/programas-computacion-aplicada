# p151-medidas-longitud.py
# Conversor de unidades de longitud

def pulgadas_a_centimetros(pulgadas: float) -> float:
    return pulgadas * 2.54

def metros_a_pies(metros: float) -> float:
    return metros * 3.281

while True:
    print("\n*** Conversor de Unidades ***")
    print("1. Pulgadas a Centímetros")
    print("2. Metros a Pies")
    print("3. Salir")

    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        continue

    if opcion == 1:
        try:
            pulgadas = float(input("Introduce la cantidad en pulgadas: "))
            resultado = pulgadas_a_centimetros(pulgadas)
            print(f"{pulgadas} pulgadas equivalen a {resultado} centímetros.")
        except ValueError:
            print("Error: Debes ingresar un valor numérico.")
    
    elif opcion == 2:
        try:
            metros = float(input("Introduce la cantidad en metros: "))
            resultado = metros_a_pies(metros)
            print(f"{metros} metros equivalen a {resultado} pies.")
        except ValueError:
            print("Error: Debes ingresar un valor numérico.")

    elif opcion == 3:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Elige entre 1 y 3.")
