# p108-conversor-unidades.py
# Conversor de unidades de longitud usando diccionarios

print('\033[H\033[J')
print('Conversor de unidades de longitud usando diccionarios\n')

conversiones = {
    'km': 1000,
    'm': 1,
    'cm': 0.01,
    'mm': 0.001
}

# Solicitar longitud válida
while True:
    try:
        longitud = float(input("Dame la longitud: "))
        break
    except ValueError:
        print("Error: Debe ingresar un valor numérico.\n")

# Solicitar unidad válida
while True:
    unidad = input("Unidad (km, m, cm, mm): ")
    if unidad.lower() in conversiones:
        unidad = unidad.lower()
        break
    else:
        print("Unidad no válida. Intente de nuevo.\n")

# Conversión
resultado = longitud * conversiones[unidad]
print(f"\n{longitud:,.2f} {unidad} son {resultado:,.2f} metros")
