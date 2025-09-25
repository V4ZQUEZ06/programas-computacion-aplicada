# p043-adivina-numero.py
# Permite múltiples intentos hasta acertar

import random

numero_secreto = random.randint(1, 50)  # Número entero al azar entre 1 y 50
contador_intentos = 0

print("¡Bienvenido al juego 'Adivina el Número'!")
print("He pensado en un número entre 1 y 50. ¿Podrás adivinarlo?")
print("------------------------------------------------------")

while True:
    intento_usuario = int(input("Tu número: "))
    contador_intentos += 1

    # Lógica de pistas
    if intento_usuario < numero_secreto:
        print("¡Demasiado bajo! Intenta con un número más alto.")
    elif intento_usuario > numero_secreto:
        print("¡Demasiado alto! Intenta con un número más bajo.")
    else:
        # ¡Es el correcto!
        print(f"\n¡Felicidades! Adivinaste el número secreto: {numero_secreto}")
        print(f"Lo lograste en {contador_intentos} intento(s).")
        break
