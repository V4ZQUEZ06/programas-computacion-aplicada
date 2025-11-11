# p137-temperatura.py
# Convertir de centígrados a Fahrenheit y viceversa

def centigrados_a_fahrenheit(c: float) -> float:
    return (c * 9/5) + 32

def fahrenheit_a_centigrados(f: float) -> float:
    return (f - 32) * 5/9

def main() -> None:
    print('Conversión de temperaturas:')
    print('1. Centígrados a Fahrenheit')
    print('2. Fahrenheit a Centígrados')
    opcion = int(input('Elige una opción (1 o 2): '))

    if opcion == 1:
        print('Dame la temperatura en Centígrados:')
        c = float(input())
        f = centigrados_a_fahrenheit(c)
        print(f'{c}°C son {f:.2f}°F')
    elif opcion == 2:
        print('Dame la temperatura en Fahrenheit:')
        f = float(input())
        c = fahrenheit_a_centigrados(f)
        print(f'{f}°F son {c:.2f}°C')
    else:
        print('Opción inválida')

if __name__ == "__main__":
    main()
