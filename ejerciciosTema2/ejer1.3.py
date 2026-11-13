
IVA: int = 21

def calculo_IVA (precio: float) -> float:
    return precio + (1 + IVA/100)

print(f"{calculo_IVA(5.99):.2f}")
print(f"{calculo_IVA(4.99):.2f}")
print(f"{calculo_IVA(9.99):.2f}")