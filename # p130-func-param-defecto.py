# p130-func-param-defecto.py

def calcular_total(monto: float, iva: float = 0.16) -> float:
    return monto + (monto * iva)

# Llama usando el valor por defecto (0.16)
print(f"Total 1: ${calcular_total(1000)}")
# Llama con un valor específico (0.08)
print(f"Total 2: ${calcular_total(1000, 0.08)}")
