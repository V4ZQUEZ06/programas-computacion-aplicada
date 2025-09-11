# p013-funciones-matematicas-precios.py
# Demostrar el uso de funciones matemáticas para redondeo y manejo de precios
import math
# Precio con decimales
precio = 21.56
# Diferentes métodos de redondeo
arriba = math.ceil(precio)
abajo = math.floor(precio)
truncado = math.trunc(precio)
redondeo = round(precio)
un_decimal = round(precio, 1)
# Mostrar resultados con formato
print(f"Precio original. : ${precio}")
print(f"Redondeo arriba (ceil): ${arriba}")
print(f"Redondeo abajo (floor): ${abajo}")
print(f"Truncado (trunc) : ${truncado}")
print(f"Redondeo normal : ${redondeo}")
print(f"Redondeo 1 decimal : ${un_decimal}")