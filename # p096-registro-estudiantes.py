# p096-registro-estudiantes.py
# Registro y análisis de asistentes a un evento

print('\033[H\033[J')
print('Sistema de Registro para Evento\n')
print("Introduce los nombres y edades de los asistentes (* en nombre para terminar)\n")

# ===== Listas paralelas =====
nombres = []
edades = []

# ===== Captura de datos =====
while True:
    nombre = input("Nombre del asistente: ").strip()
    if nombre == "*":
        break  # Termina el ciclo si el nombre es *
    if not nombre:
        print("El nombre no puede estar vacío.")
        continue

    try:
        edad = int(input(f"Edad de {nombre}: "))
        nombres.append(nombre)
        edades.append(edad)
    except ValueError:
        print("Por favor, introduce una edad válida (número entero).")

# ===== Reportes =====
if not nombres:
    print("\nNo se registraron asistentes.")
else:
    # 1️⃣ Asistentes mayores de edad
    print("\n--- Asistentes Mayores de Edad ---")
    encontrados = False
    for i in range(len(nombres)):
        if edades[i] >= 18:
            print(f"Nombre: {nombres[i]:<15}  Edad: {edades[i]}")
            encontrados = True
    if not encontrados:
        print("No hay asistentes mayores de edad.")

    # 2️⃣ Asistente con mayor edad
    edad_maxima = max(edades)
    pos_max = edades.index(edad_maxima)
    nombre_max = nombres[pos_max]

    print("\n--- Reconocimiento al Asistente de Mayor Edad ---")
    print(f"🏅 El asistente de mayor edad es: {nombre_max} con {edad_maxima} años.")

    # 3️⃣ Estadísticas opcionales
    promedio = sum(edades) / len(edades)
    print("\n--- Estadísticas Generales ---")
    print(f"Total de asistentes: {len(nombres)}")
    print(f"Edad promedio      : {promedio:.2f}")
    print(f"Edad mínima        : {min(edades)}")
    print(f"Edad máxima        : {max(edades)}")
