# p001-hola-mundo.py
# Lee datos y envía un saludo

print("Leyendo datos y enviando un saludo: \n")

nombre = input("Dame tu nombre : ")
edad = int(input("Dame tu Edad : "))
peso = float(input("Dame tu Peso : "))

print(f"\n{nombre}, bienvenido a Python. Tu edad es {edad} años y tu peso es {peso} kg.\n")

# Verificación de tipos
print("Tipos de datos capturados:")
print("nombre ->", type(nombre))
print("edad   ->", type(edad))
print("peso   ->", type(peso))