DESCUENTO : int = 15
precio : float = float(input("Precio: "))
total: float = precio - (precio*(DESCUENTO/100))

print(f"El precio aplicando el descuento es de: {total}")