# p066_PrimerExamenParcial.py
# Computación Aplicada - Primer Examen Parcial
# Autor: Yahir Vazquez Puente
# Fecha: 03/10/25

# Objetivo:
#   Administrar la venta de boletos de una función especial en un cine.
#   Controla el aforo, valida edad (clasificación B: >= 13 años), calcula estadísticas e ingresos
#   y muestra un mensaje final de rentabilidad.

# Requerimientos cubiertos:
# 1) Solicitar por venta: edad, tipo de comprador, sexo. (1 boleto por persona)
# 2) Precios: Estudiante $50, Adulto $90, Tercera Edad $60, Académico $70
# 3) Estadísticas: totales por tipo, por sexo, asistentes, promedio edad, rechazados
# 4) Ingresos por tipo y total
# 5) Mensaje final de rentabilidad según total recaudado
# 6) Preguntas teóricas: deja tus respuestas al final de este archivo (sección marcada)
#
# Nota: "Gestionar el aforo": al inicio se pide la capacidad de la sala (asientos disponibles).
#       Las ventas se detienen al agotarse el aforo o cuando el usuario decida terminar.

# =========================
#  Constantes y utilidades
# =========================

print("*" * 60)
print("  ADMINISTRACIÓN DE VENTAS - FUNCIÓN ESPECIAL (Clasificación B)")
print("*" * 60)

# ------------------------------------
# Entradas iniciales: AFORO DE LA SALA
# ------------------------------------
aforo_valido = False
while aforo_valido == False:
    dato = input("\nCapacidad (asientos disponibles) de la sala: ").strip()
    if dato.isdigit():
        aforo = int(dato)
        if aforo >= 1:
            aforo_valido = True
        else:
            print("  >> Error: la capacidad debe ser >= 1.")
    else:
        print("  >> Error: debes capturar un número entero válido.")

# ------------------------------------
# Inicialización de contadores y sumas
# ------------------------------------
boletos_vendidos = 0

c_est = 0  # Estudiante
c_adt = 0  # Adulto
c_3ed = 0  # Tercera Edad
c_acd = 0  # Académico

c_h = 0    # Hombres
c_m = 0    # Mujeres

rechazados_edad = 0
suma_edades = 0  # para promedio de asistentes

# Precios (constantes simples)
precio_est = 50
precio_adt = 90
precio_3ed = 60
precio_acd = 70

continuar_ventas = "S"

# ====================================
# Ciclo de ventas
# ====================================
while continuar_ventas == "S":
    print("\n---------------------------------------------")
    print("Boletos vendidos:", boletos_vendidos, "/", aforo)

    if boletos_vendidos >= aforo:
        print(">> Aforo completo. No hay asientos disponibles.")
        break

    # Edad
    edad_valida = False
    while edad_valida == False:
        d = input("Edad del comprador: ").strip()
        if d.isdigit():
            edad = int(d)
            if edad >= 0:
                edad_valida = True
            else:
                print("  >> Error: edad inválida.")
        else:
            print("  >> Error: debes capturar un número entero válido.")

    # Clasificación B: >= 13 años
    if edad < 13:
        print("ACCESO DENEGADO: El comprador es menor de 13 años.")
        rechazados_edad = rechazados_edad + 1

        # Preguntar si continuamos
        seguir = ""
        while not (seguir == "S" or seguir == "N"):
            seguir = input("¿Registrar otra venta? (S/N): ").strip().upper()
            if not (seguir == "S" or seguir == "N"):
                print("  >> Responde con 'S' o 'N'.")
        if seguir == "N":
            break
        else:
            continue  # no ocupa asiento, no cuenta venta

    # Tipo de comprador (1-4)
    print("\nTipos de comprador:")
    print("  1) Estudiante ($50)")
    print("  2) Adulto ($90)")
    print("  3) Tercera Edad ($60)")
    print("  4) Académico ($70)")
    tipo_ok = False
    while tipo_ok == False:
        t = input("Elige el tipo (1-4): ").strip()
        if t.isdigit():
            op = int(t)
            if op >= 1 and op <= 4:
                tipo_ok = True
                if op == 1:
                    tipo_texto = "Estudiante"
                elif op == 2:
                    tipo_texto = "Adulto"
                elif op == 3:
                    tipo_texto = "Tercera Edad"
                else:
                    tipo_texto = "Académico"
            else:
                print("  >> Error: elige un número entre 1 y 4.")
        else:
            print("  >> Error: elige un número entre 1 y 4.")

    # Sexo (H/M o palabra)
    sexo_valido = False
    while sexo_valido == False:
        sx = input("Sexo (Hombre/Mujer) [H/M]: ").strip().upper()
        if sx == "H" or sx == "HOMBRE":
            sexo = "HOMBRE"
            sexo_valido = True
        elif sx == "M" or sx == "MUJER":
            sexo = "MUJER"
            sexo_valido = True
        else:
            print("  >> Error: escribe H/M o Hombre/Mujer.")

    # Registrar venta
    boletos_vendidos = boletos_vendidos + 1
    suma_edades = suma_edades + edad

    # Contadores por tipo
    if tipo_texto == "Estudiante":
        c_est = c_est + 1
    elif tipo_texto == "Adulto":
        c_adt = c_adt + 1
    elif tipo_texto == "Tercera Edad":
        c_3ed = c_3ed + 1
    else:
        c_acd = c_acd + 1

    # Contadores por sexo
    if sexo == "HOMBRE":
        c_h = c_h + 1
    else:
        c_m = c_m + 1

    # Mensaje de bienvenida
    print("¡Bienvenido(a)! Venta registrada: Edad", edad, ", Sexo", sexo, ", Tipo", tipo_texto + ".")

    if boletos_vendidos >= aforo:
        print(">> Aforo completo. Fin de ventas.")
        break

    # ¿Seguir?
    continuar_ventas = ""
    while not (continuar_ventas == "S" or continuar_ventas == "N"):
        continuar_ventas = input("¿Registrar otra venta? (S/N): ").strip().upper()
        if not (continuar_ventas == "S" or continuar_ventas == "N"):
            print("  >> Responde con 'S' o 'N'.")

# ====================================
# Reporte final
# ====================================
print("\n" + "*" * 35)
print("*** REPORTE FINAL DE LA FUNCIÓN ***")
print("*" * 35)

print("--- Estadísticas del Público ---")
print("Total de Estudiantes:", c_est)
print("Total de Adultos:", c_adt)
print("Total de Tercera Edad:", c_3ed)
print("Total de Académicos:", c_acd)
print("-------------------------------")
print("Total de Hombres:", c_h)
print("Total de Mujeres:", c_m)
print("-------------------------------")

asistentes = c_est + c_adt + c_3ed + c_acd
print("Total de Asistentes:", asistentes)

if asistentes > 0:
    promedio = suma_edades / asistentes
    # Mostrar con 2 decimales sin usar round()
    print("Promedio de edad de asistentes: " + "{0:.2f}".format(promedio) + " años")
else:
    print("Promedio de edad de asistentes: 0.00 años")

print("Personas rechazadas por edad:", rechazados_edad)

# Ingresos por tipo
ing_est = c_est * precio_est
ing_adt = c_adt * precio_adt
ing_3ed = c_3ed * precio_3ed
ing_acd = c_acd * precio_acd
total_ingresos = ing_est + ing_adt + ing_3ed + ing_acd

print("--- Reporte de Ingresos ---")
print("Ingresos por Estudiantes: $" + "{0:.2f}".format(ing_est))
print("Ingresos por Adultos: $" + "{0:.2f}".format(ing_adt))
print("Ingresos por Tercera Edad: $" + "{0:.2f}".format(ing_3ed))
print("Ingresos por Académicos: $" + "{0:.2f}".format(ing_acd))
print("-------------------------------")
print("TOTAL RECAUDADO: $" + "{0:.2f}".format(total_ingresos))

# Rentabilidad
print("--- Rentabilidad ---")
if total_ingresos < 1500:
    print("La función generó BAJAS ganancias.")
elif total_ingresos >= 1500 and total_ingresos <= 3500:
    print("La función generó ganancias MODERADAS.")
else:
    print("La función generó BUENAS ganancias.")

# 1) Diferencia entre 'while' y 'for' y cuándo usar cada uno.
# 'while' se repite mientras una condición sea verdadera; no se sabe cuántas veces
# repetirá y se usa comunmente cuando el número de iteraciones depende de algo que cambia
# durante la ejecución. En este programa utilizamos 'while' para:
#   - Validar que aforo y edad sean números válidos.
#   - Repetir las ventas hasta llenar aforo o elegir terminar.
# 'for' recorre una secuencia conocida con un número de
# iteraciones predecible. 

# 2) ¿Qué es una variable y qué es una constante? Ejemplos del programa.
# Variable: espacio en la memoria que puede cambiar de valor durante el programa.
# Ejemplos: boletos_vendidos, c_est, c_adt, c_3ed, c_acd, c_h, c_m,
#           rechazados_edad, suma_edades, asistentes, total_ingresos.
# Constante: valor que no debe cambiar mientras corre el programa.
# En este ejercicio las tratamos como "constantes lógicas" usando nombres fijos:
#   precio_est = 50, precio_adt = 90, precio_3ed = 60, precio_acd = 70.


# 3) ¿Qué es la validación de entrada y por qué es importante?
# Es revisar que lo que escribe el usuario cumpla con lo esperado (tipo y rango).
# Evita fallas (crashes) y resultados incorrectos. Aquí validamos que aforo y edad
# sean números enteros (usando .isdigit()) y que aforo sea >= 1. También validamos
# opciones (tipo 1-4, sexo H/M) con while hasta que el usuario ingrese algo válido.

# 4) ¿Cómo calcular el promedio y evitar división entre cero?
# Promedio = suma / cantidad. En el programa, usamos:
#   promedio = suma_edades / asistentes
# Para evitar división entre cero primero verificamos:
#   if asistentes > 0:
#       promedio = suma_edades / asistentes
#   else:
#       promedio = 0 (o mostramos 0.00)
# Así nunca dividimos entre 0 cuando no hubo asistentes.

# 5) ¿Cómo estructuraste este programa (secciones y acumuladores)?
# - Encabezado y mensaje inicial.
# - Entrada inicial del aforo (con validación).
# - Inicialización de acumuladores:
#   c_est, c_adt, c_3ed, c_acd (por tipo), c_h, c_m (por sexo),
#   boletos_vendidos, rechazados_edad, suma_edades.
# - Ciclo principal de ventas (while):
#     * Pide edad (valida) y verifica clasificación B (>=13).
#     * Si válido: pide tipo (1-4) y sexo (H/M), suma contadores e imprime bienvenida.
#     * Verifica aforo o si el usuario desea continuar.
# - Reporte final:
#     * Totales por tipo y sexo, asistentes, rechazados.
#     * Promedio de edad (solo si asistentes > 0).
#     * Ingresos por tipo y total.
#     * Mensaje de rentabilidad según total recaudado.

