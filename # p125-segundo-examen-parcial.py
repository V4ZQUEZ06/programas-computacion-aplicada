# ============================================================
# 🧮 p125-segundo-examen-parcial.py
# TecnoTienda - Sistema de Inventario
# Autor: Yahir Vazquez Puente
# Descripción:
#   Programa que captura productos electrónicos y genera un
#   resumen estadístico del inventario.
# ============================================================

# ==========================
# 1️⃣ Captura de productos
# ==========================
productos = []  # Lista donde se almacenarán los diccionarios

print("=== 🛒 TecnoTienda - Sistema de Inventario ===")
print("Ingrese los datos de los productos (deje el nombre vacío para terminar)\n")

while True:
    nombre = input("Nombre del producto: ").strip()
    if nombre == "":  # Condición de salida
        break

    # Se solicita el resto de datos y se validan
    try:
        precio = float(input("Precio: "))
        categoria = input("Categoría (Laptops, Celulares, Audio...): ").capitalize()
        proveedor = input("Proveedor: ").capitalize()
        stock = int(input("Stock: "))
    except ValueError:
        print("⚠️ Error: Ingrese valores válidos. Reiniciando producto...\n")
        continue

    # Se crea un diccionario por producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "categoria": categoria,
        "proveedor": proveedor,
        "stock": stock
    }

    # Se agrega a la lista principal
    productos.append(producto)
    print("✅ Producto agregado correctamente.\n")


# ==========================
# 2️⃣ Datos crudos
# ==========================
print("\n" + "="*60)
print("📋 DATOS CRUDOS (LISTA DE DICCIONARIOS):")
print(productos)


# ==========================
# 3️⃣ Formato Tabular
# ==========================
print("\n" + "="*60)
print("📊 TABLA DE DATOS:\n")
print(f"{'Nombre':20s} {'Precio':>10s} {'Categoría':15s} {'Stock':>7s} {'Proveedor':15s}")
print("-"*70)
for p in productos:
    print(f"{p['nombre']:20s} {p['precio']:10.2f} {p['categoria']:15s} {p['stock']:7d} {p['proveedor']:15s}")


# ==========================
# 4️⃣ Resumen del inventario
# ==========================
print("\n" + "="*60)
print("📈 RESUMEN DEL INVENTARIO:\n")

total_productos = len(productos)
print(f"Total de productos registrados: {total_productos}")

# --- Contar productos por categoría ---
categorias = {}
for p in productos:
    categorias[p["categoria"]] = categorias.get(p["categoria"], 0) + 1

print("\nCategorías:")
for c, n in categorias.items():
    print(f" • {c}: {n}")

# --- Contar productos por proveedor ---
proveedores = {}
for p in productos:
    proveedores[p["proveedor"]] = proveedores.get(p["proveedor"], 0) + 1

print("\nProveedores:")
for prov, n in proveedores.items():
    print(f" • {prov}: {n}")

# --- Calcular sumas y promedios ---
suma_stock = sum(p["stock"] for p in productos)
prom_stock = suma_stock / total_productos if total_productos > 0 else 0

suma_precios = sum(p["precio"] for p in productos)
prom_precios = suma_precios / total_productos if total_productos > 0 else 0

print(f"\nStock → Suma: {suma_stock}, Promedio: {prom_stock:.2f}")
print(f"Precio → Suma: {suma_precios:,.2f}, Promedio: {prom_precios:,.2f}")

# --- Producto más caro y más barato ---
if productos:
    mas_caro = max(productos, key=lambda x: x["precio"])
    mas_barato = min(productos, key=lambda x: x["precio"])
    print(f"\n💎 Más caro: {mas_caro['nombre']} (${mas_caro['precio']:,.2f})")
    print(f"🪙 Más barato: {mas_barato['nombre']} (${mas_barato['precio']:,.2f})")

print("\n✅ Fin del procesamiento de inventario.")
