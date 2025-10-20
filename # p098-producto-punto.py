# p098-producto-punto.py
# Cálculo del producto punto de dos vectores

print('\033[H\033[J')
print("--- Cálculo del Producto Punto ---\n")

# ===== Vectores =====
vector_a = [1, 3, -5]
vector_b = [4, -2, -1]
producto_punto = 0

print(f"Vector A: {vector_a}")
print(f"Vector B: {vector_b}\n")

# ===== Verificar longitud =====
if len(vector_a) == len(vector_b):
    # Multiplicar elementos y sumar resultados
    for i in range(len(vector_a)):
        producto = vector_a[i] * vector_b[i]
        producto_punto += producto
        print(f"  Paso {i+1}: {vector_a[i]} × {vector_b[i]} = {producto}")

    # Mostrar resultado final
    print(f"\n➡️ El producto punto de los vectores es: {producto_punto}")
    print("\n(El cálculo sería: (1×4) + (3×−2) + (−5×−1) = 4 − 6 + 5 = 3)")
else:
    print("❌ Error: Los vectores deben tener la misma longitud para calcular el producto punto.")
