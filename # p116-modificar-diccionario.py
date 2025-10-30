# p116-modificar-diccionario.py
# Modificar valores dentro de un diccionario

print('\033[H\033[J')

# Diccionario inicial
paises = {
    'Argentina': 100,
    'Brasil': 200,
    'Colombia': 300,
    'Chile': 400,
    'Ecuador': 500,
    'Bolivia': 600,
    'Jamaica': 700
}

print("Diccionario inicial:")
print(paises)

# Modificaciones
paises['Brasil'] = 250     # usando []
paises['Chile'] = 450      # usando []
paises.update({'Bolivia': 650})  # usando update()
paises.update({'Jamaica': 750})  # usando update()

print("\nDiccionario modificado:")
print(paises)
