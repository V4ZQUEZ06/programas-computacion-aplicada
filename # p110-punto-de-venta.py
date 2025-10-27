# p110-punto-de-venta.py
# Simulación de un punto de venta usando diccionarios

print('\033[H\033[J')
print('Simulación de un punto de venta usando diccionarios\n')

menu = {
    'taco': 18.50,
    'burrito': 45.00,
    'quesadilla': 35.00,
    'refresco': 20.00,
    'agua': 15.00
}

print("--- Bienvenido a 'El Taco Feroz' ---")
print("Este es nuestro menú:\n")

for item, precio in menu.items():
    print(f" - {item:<12} : ${precio:,.2f}")

print("-" * 35)

orden = {}
total_general = 0

# Captura de la orden
while True:
    producto = input("\n¿Qué desea ordenar? (escriba 'fin' para terminar): ").lower()

    if producto == 'fin':
        break

    if producto not in menu:
        print("⚠️ Error: Ese producto no está en el menú. Intente de nuevo.")
        continue

    try:
        cantidad = int(input(f"¿Cuántos '{producto}' desea?: "))
        if cantidad <= 0:
            print("⚠️ Error: La cantidad debe ser positiva.")
            continue
    except ValueError:
        print("⚠️ Error: Debe ingresar un número entero (ej. 2).")
        continue

    orden[producto] = orden.get(producto, 0) + cantidad
    print(f"✅ Agregados {cantidad} '{producto}'(s) a su orden.")

# Impresión del recibo
print("\n--- SU RECIBO ---")

if not orden:
    print("No se ordenó ningún producto.")
else:
    for producto, cantidad in orden.items():
        precio_unitario = menu[producto]
        subtotal = precio_unitario * cantidad
        total_general += subtotal
        print(f" {cantidad} x {producto:<12} : ${subtotal:,.2f}")

    print("-" * 35)
    print(f"TOTAL A PAGAR: ${total_general:,.2f}")
    print("¡Gracias por su compra! 😄")

