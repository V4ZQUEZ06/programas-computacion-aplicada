# p056-contador-vocales.py
# Cuenta las vocales y consonantes en una frase y otros caracteres

while True:
    print('\033[H\033[J')  # Limpia pantalla
    print("Contador de Vocales y Consonantes")

    frase = input("\nIntroduce una frase: ").lower()
    vocales = 0
    consonantes = 0
    otros = 0
    indice = 0

    while indice < len(frase):
        caracter = frase[indice]
        # Verificar si es una letra del alfabeto
        if 'a' <= caracter <= 'z':
            if caracter in "aeiou":
                vocales += 1
            else:
                consonantes += 1
        else:
            otros += 1
        indice += 1

    print(f"\nAnálisis de la frase:")
    print(f"Número de vocales: {vocales}")
    print(f"Número de consonantes: {consonantes}")
    print(f"Número de caracteres no alfabéticos: {otros}")

    if input("\n¿Deseas analizar otra frase (S/N)? ").upper() == "N":
        break

print("\nFin del programa. ¡Gracias!")
