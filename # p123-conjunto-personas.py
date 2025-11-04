# p123-conjunto-personas.py
# Operaciones con conjuntos de personas

print('\033[H\033[J')  # Limpia pantalla en consola

# Listas iniciales
lista1 = ["Juan", "Maria", "Pedro", "Jose", "Rocio"]
lista2 = ["Pedro", "Juan", "Pablo", "Mateo", "Esther"]

# Crear conjuntos A y B
A = set(lista1)
B = set(lista2)

# Mostrar conjuntos
print("--- Conjuntos Base ---")
print(f"A (Lista 1): {A}")
print(f"B (Lista 2): {B}")

# Operaciones
print("\n--- Operaciones entre conjuntos ---")
print(f"Unión (A | B): {A | B}")
print(f"Intersección (A & B): {A & B}")
print(f"Diferencia (A - B): {A - B}")
print(f"Diferencia Simétrica (A ^ B): {A ^ B}")

# Verificaciones
print("\n--- Verificaciones de subconjuntos y pertenencia ---")
print(f"¿{{'Pablo', 'Mateo'}} es subconjunto de B?: {{'Pablo', 'Mateo'}} <= B = { {'Pablo', 'Mateo'} <= B }")
print(f"¿A es superconjunto de {{'Reynaldo', 'Angelica'}}?: A >= {{'Reynaldo', 'Angelica'}} = { A >= {'Reynaldo', 'Angelica'} }")
print(f"¿'Pedro' está en A?: {'Pedro' in A}")
print(f"¿'Lilia' NO está en B?: {'Lilia' not in B}")
