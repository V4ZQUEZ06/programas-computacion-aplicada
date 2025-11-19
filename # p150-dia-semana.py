# p150-dia-semana.py
# Función que recibe un número del 1 al 7 y devuelve el día correspondiente

def dia_semana(numero: int) -> str:
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }

    if numero in dias:
        return dias[numero]
    else:
        return "Error: El número debe estar entre 1 y 7."

# Programa principal
try:
    num = int(input("Introduce un número del 1 al 7: "))
    resultado = dia_semana(num)
    print(f"El día es: {resultado}" if "Error" not in resultado else resultado)

except ValueError:
    print("Error: Debes ingresar un número entero.")
