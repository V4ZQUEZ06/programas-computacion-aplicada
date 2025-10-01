# p065-SistemaPapeleria.py
# Autor: Yahir Vazquez Puente
# Objetivos:
#   Sistema de ventas de copias para una papelería.
#   - Registra múltiples ventas (tipo y cantidad).
#   - Aplica 10% de descuento por transacción si la cantidad > 50.
#   - Calcula subtotales por tipo y total general.
#   - Muestra “precio original” por tipo cuando hubo descuento.
#   - Clasifica el desempeño del día según el total vendido.
#
# Secciones:
#   Entradas: tipo de copia y cantidad por venta (hasta terminar).
#   Proceso : cálculo de importes con/sin descuento y acumulados.
#   Salidas : resumen detallado y mensaje de desempeño.

# -------------------------
# PRECIOS (constantes)
# -------------------------
precioC = 3.00   # Carta
precioO = 4.00   # Oficio
precioD = 6.00   # Doble Of.
precioP = 12.00  # Plano
descuentoVol = 0.10  # 10%

while True:
    # Limpia pantalla (opcional, terminal compatible ANSI)
    print('\033[H\033[J', end='')

    print("---------------------------------")
    print("Papelería la Malena, SA. de CV.")
    print("Sistema de ventas de copias")
    print("---------------------------------")

    # -------------------------
    # Acumuladores por tipo
    # -------------------------
    cantC = 0; cantO = 0; cantD = 0; cantP = 0
    realC = 0.0; realO = 0.0; realD = 0.0; realP = 0.0
    origC = 0.0; origO = 0.0; origD = 0.0; origP = 0.0

    ventas_realizadas = 0

    # ==============
    # ENTRADAS/PROCESO
    # ==============
    while True:
        ventas_realizadas += 1
        print("Venta:", ventas_realizadas)

        # ---- Tipo de copia ----
        tipo = input("Tipo de copia (C)arta $3, (O)ficio $4, (D)oble Of $6, (P)lano $12 ? ").strip().upper()
        while not (tipo == "C" or tipo == "O" or tipo == "D" or tipo == "P"):
            print("Error: tipo inválido. Intenta con C, O, D o P.")
            tipo = input("Tipo de copia (C)arta $3, (O)ficio $4, (D)oble Of $6, (P)lano $12 ? ").strip().upper()

        # ---- Cantidad ----
        ok = False
        while ok == False:
            entrada = input("Cantidad ? ").strip()
            # Validar entero positivo usando while/if
            es_numero = True
            i = 0
            if len(entrada) == 0:
                es_numero = False
            else:
                # permitir solo dígitos
                while i < len(entrada):
                    if not ('0' <= entrada[i] <= '9'):
                        es_numero = False
                        break
                    i += 1
            if es_numero == True:
                cantidad = int(entrada)
                if cantidad > 0:
                    ok = True
                else:
                    print("La cantidad debe ser un entero positivo.")
            else:
                print("Entrada inválida. Escribe un número entero.")

        # ---- Precio unitario según tipo ----
        # (solo if/elif/else)
        if tipo == "C":
            pUnit = precioC
        elif tipo == "O":
            pUnit = precioO
        elif tipo == "D":
            pUnit = precioD
        else:
            pUnit = precioP

        # ---- Cálculo de importes ----
        importeOriginal = cantidad * pUnit
        importeReal = importeOriginal

        if cantidad > 50:
            importeReal = round(importeOriginal * (1 - descuentoVol), 2)
            print("*** Descuento del 10% aplicado por volumen! ***")

        # ---- Acumular por tipo ----
        if tipo == "C":
            cantC = cantC + cantidad
            origC = origC + importeOriginal
            realC = realC + importeReal
        elif tipo == "O":
            cantO = cantO + cantidad
            origO = origO + importeOriginal
            realO = realO + importeReal
        elif tipo == "D":
            cantD = cantD + cantidad
            origD = origD + importeOriginal
            realD = realD + importeReal
        else:
            cantP = cantP + cantidad
            origP = origP + importeOriginal
            realP = realP + importeReal

        # ---- Otra venta ----
        otra = input("Otra venta (S/N) ? ").strip().upper()
        if otra == "N":
            break

    # =========
    # SALIDAS
    # =========
    print('\033[H\033[J', end='')
    print("---------------------------------------")
    print("Resumen diario de ventas")
    print("---------------------------------------")
    print("Ventas realizadas:", ventas_realizadas)
    print("-------------------------")

    # Totales
    totalUnidades = cantC + cantO + cantD + cantP
    totalRecaudado = realC + realO + realD + realP

    # Carta
    if cantC == 0:
        print("Carta     : 0 - $ 0.00")
    else:
        if round(realC, 2) < round(origC, 2):
            print("Carta     :", cantC, "- $", f"{realC:,.2f}", "(Precio original: $"+f"{origC:,.2f}"+")")
        else:
            print("Carta     :", cantC, "- $", f"{realC:,.2f}")

    # Oficio
    if cantO == 0:
        print("Oficio    : 0 - $ 0.00")
    else:
        if round(realO, 2) < round(origO, 2):
            print("Oficio    :", cantO, "- $", f"{realO:,.2f}", "(Precio original: $"+f"{origO:,.2f}"+")")
        else:
            print("Oficio    :", cantO, "- $", f"{realO:,.2f}")

    # Doble Of.
    if cantD == 0:
        print("Doble Of. : 0 - $ 0.00")
    else:
        if round(realD, 2) < round(origD, 2):
            print("Doble Of. :", cantD, "- $", f"{realD:,.2f}", "(Precio original: $"+f"{origD:,.2f}"+")")
        else:
            print("Doble Of. :", cantD, "- $", f"{realD:,.2f}")

    # Plano
    if cantP == 0:
        print("Plano     : 0 - $ 0.00")
    else:
        if round(realP, 2) < round(origP, 2):
            print("Plano     :", cantP, "- $", f"{realP:,.2f}", "(Precio original: $"+f"{origP:,.2f}"+")")
        else:
            print("Plano     :", cantP, "- $", f"{realP:,.2f}")

    print("-------------------------")
    print("Tot. Ventas :", totalUnidades, "- $", f"{totalRecaudado:,.2f}")

    # Mensaje de desempeño (solo if/elif/else)
    if totalRecaudado < 50:
        print("Esta venta es una : Venta Moderada")
    elif totalRecaudado <= 150:
        print("Esta venta es una : Venta Frecuente")
    else:
        print("Esta venta es una : Venta superada")

    # Reiniciar día o terminar
    fin = input("\n¿Desea iniciar un nuevo día (S/N)? ").strip().upper()
    if fin == "N":
        break

print("\nGracias por usar el sistema. ¡Hasta pronto!")

