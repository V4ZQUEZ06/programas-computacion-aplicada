# p120-contar-caracteres.py
# Contar frecuencia de caracteres en una cadena

print('\033[H\033[J')

# Solicitar cadena al usuario
cadena = input("Ingrese una cadena: ")

# Diccionario vacío para contar caracteres
frecuencia = {}

# Recorrer cada carácter en la cadena
for c in cadena:
    if c in frecuencia:
        frecuencia[c] += 1
    else:
        frecuencia[c] = 1

# Mostrar resultado
print("\nResultado:")
print(frecuencia)
