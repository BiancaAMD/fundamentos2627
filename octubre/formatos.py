'''
producto: str = "Camisa"
unidades: int = 3
precio: float = 19.95

base: float = unidades * precio
iva: float = base * 21 / 100
total: float = base + iva

print(producto, unidades, precio)
print(base, iva, total)
'''

producto: str = input("Producto: ")
unidades: int = int(input("Unidades: "))
precio: float = float(input("Precio:   "))

base: float = unidades * precio
iva: float = base * 21 / 100
total: float = base + iva

print()
print(f"{'Base':<12}{base:>8.2f}")
print(f"{'IVA (21%)':<12}{iva:>8.2f}")
print("-" * 20)
print(f"{'TOTAL':<12}{total:>8.2f}")

