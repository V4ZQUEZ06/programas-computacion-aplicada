# p140-promedio-letra.py
# Recibe un promedio y regresa: una letra y un mensaje (tupla)

def calificacion_a_letra(promedio: float) -> tuple[str, str]:
    if 90 <= promedio <= 100:
        return 'A', 'Excelente'
    elif 80 <= promedio < 90:
        return 'B', 'Bien'
    elif 70 <= promedio < 80:
        return 'C', 'Suficiente'
    elif 60 <= promedio < 70:
        return 'D', 'Deficiente'
    elif 0 <= promedio < 60:
        return 'F', 'Reprobado'
    else:
        return 'Calificación inválida', ''

def main() -> None:
    promedio = float(input("Introduce el promedio (0-100): "))
    letra, mensaje = calificacion_a_letra(promedio)
    if mensaje:
        print(f"Calificación: {letra} - {mensaje}")
    else:
        print(letra)

if __name__ == "__main__":
    main()
