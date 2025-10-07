# p075-cifrado-cesar.py
# Cifra un mensaje usando el Cifrado César.

while True:
    print('\033[H\033[J')
    print('Encriptador con Cifrado César')

    mensaje_original = input("Ingresa el mensaje a encriptar: ")
    desplazamiento = int(input("Ingresa la clave de desplazamiento (un número): "))

    mensaje_cifrado = ""

    for caracter in mensaje_original:
        if caracter.isalpha():  # Solo ciframos las letras
            codigo_ascii = ord(caracter)
            # Verificamos si es mayúscula o minúscula para mantener el caso
            base = ord('a') if caracter.islower() else ord('A')
            # Aplicamos la fórmula del cifrado
            codigo_nuevo = base + (codigo_ascii - base + desplazamiento) % 26
            mensaje_cifrado += chr(codigo_nuevo)
        else:
            mensaje_cifrado += caracter  # Los otros caracteres pasan igual

    print(f"\nMensaje Original: {mensaje_original}")
    print(f"Mensaje Cifrado: {mensaje_cifrado}")

    if input('\n\n¿Deseas encriptar otro mensaje (S/N)? ').upper() == 'N':
        break

print('\n¡Encriptación finalizada!')
