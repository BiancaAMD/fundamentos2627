def media(numeros: list[float]) -> float: 
    if len(numeros)==0:
        return 0.0
    return sum(numeros)/ len(numeros)

print(media([1,2,3,4,5]))
print(media([]))
    