IVA: int = 21

precio: float = 80.0
conIva: float = precio * (1+IVA/100)

print(f"{conIva:.2f}")