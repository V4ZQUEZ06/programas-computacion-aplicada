# p065-SistemaPapeleria.py
# Autor: Yahir Vazquez Puente 
# Objetivos:
#   Sistema para gestionar ventas de fotocopias en una papelería.
#   - Registra múltiples ventas (tipo y cantidad).
#   - Aplica 10% de descuento por transacción si la cantidad > 50.
#   - Calcula subtotales por tipo y total general (con descuento aplicado).
#   - Muestra “precio original” por tipo cuando hubo descuentos.
#   - Clasifica el desempeño del día según el total vendido.
#
# Secciones:
#   Entradas: tipo de copia y cantidad por venta (hasta que el usuario decida parar).
#   Proceso : cálculo de importes con/ sin descuento y acumulados.
#   Salidas : resumen detallado y mensaje de desempeño.

def limpiar_pantalla():
    # Limpieza simple para terminales compatibles ANSI
    print('\033[H\033[J', end='')

# -------------------------
# Precios por tipo de copia
# -------------------------
PRECIOS = {
    'C': ('Carta', 3.00),
    'O': ('Oficio', 4.00),
    'D': ('Doble Of.', 6.00),
    'P': ('Plano', 12.00)
}

DESCUENTO_VOL = 0.10  # 10% por transacción cuando cantidad > 50

def pedir_tipo():
    while True:
        t = input("Tipo de copia (C)arta $3, (O)ficio $4, (D)oble Of $6, (P)lano $12 ? ").strip().upper()
        if t in PRECIOS:
            return t
        print("Error: tipo inválido. Intenta con C, O, D o P.")

def pedir_cantidad():
    while True:
        try:
            c = int(input("Cantidad ? ").strip())
            if c > 0:
                return c
            print("La cantidad debe ser un entero positivo.")
        except ValueError:
            print("Entrada inválida. Escribe un número entero.")

def mensaje_desempeno(total):
    if total < 50:
        return "Venta Moderada"
    elif total <= 150:
        return "Venta Frecuente"
    else:
        return "Venta superada"

while True:
    limpiar_pantalla()
    print("---------------------------------")
    print("Papelería la Malena, SA. de CV.")
    print("Sistema de ventas de copias")
    print("---------------------------------")

    # Acumuladores por tipo:
    # - cantidades
    # - total con descuento aplicado (recaudación real)
    # - total “precio original” (sin descuento) para informar si hubo descuento
    cantidades = {k: 0 for k in PRECIOS}
    subtotal_real = {k: 0.0 for k in PRECIOS}
    subtotal_original = {k: 0.0 for k in PRECIOS}

    ventas_realizadas = 0

    # -----------------
    # ENTRADAS / PROCESO
    # -----------------
    while True:
        ventas_realizadas += 1
        print(f"Venta: {ventas_realizadas}")
        tipo = pedir_tipo()
        nombre_tipo, precio_unit = PRECIOS[tipo]
        cant = pedir_cantidad()

        importe_original = cant * precio_unit
        importe_real = importe_original

        # Descuento por volumen por transacción
        if cant > 50:
            importe_real = round(importe_original * (1 - DESCUENTO_VOL), 2)
            print("*** Descuento del 10% aplicado por volumen! ***")

        # Acumular por tipo
        cantidades[tipo] += cant
        subtotal_original[tipo] += importe_original
        subtotal_real[tipo] += importe_real

        # Otra venta
        op = input("Otra venta (S/N) ? ").strip().upper()
        if op == 'N':
            break

    # -----------
    # SALIDAS
    # -----------
    limpiar_pantalla()
    print("---------------------------------------")
    print("Resumen diario de ventas")
    print("---------------------------------------")
    print(f"Ventas realizadas: {ventas_realizadas}")
    print("-------------------------")

    total_unidades = 0
    total_recaudado = 0.0

    # Imprimir en el orden C, O, D, P
    for clave in ['C', 'O', 'D', 'P']:
        nombre, _ = PRECIOS[clave]
        cant = cantidades[clave]
        real = subtotal_real[clave]
        orig = subtotal_original[clave]

        total_unidades += cant
        total_recaudado += real

        if cant == 0:
            print(f"{nombre:<9}: {cant} - $ {0.00:,.2f}")
        else:
            # Si hubo algún descuento en este tipo (es decir, real < orig), mostrar el original
            if round(real, 2) < round(orig, 2):
                print(f"{nombre:<9}: {cant} - $ {real:,.2f} (Precio original: ${orig:,.2f})")
            else:
                print(f"{nombre:<9}: {cant} - $ {real:,.2f}")

    print("-------------------------")
    print(f"Tot. Ventas : {total_unidades} - $ {total_recaudado:,.2f}")
    print(f"Esta venta es una : {mensaje_desempeno(total_recaudado)}")

    # Finalizar o reiniciar el día
    fin = input("\n¿Desea iniciar un nuevo día (S/N)? ").strip().upper()
    if fin == 'N':
        break

print("\nGracias por usar el sistema. ¡Hasta pronto!")
