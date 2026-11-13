def suma_lista(numeros: list[float]) -> float:
    total: float = 0.0
    for i in numeros:
        total = total + i
    return total

print(f"Suma: {suma_lista([1,2,3,4,5])}")