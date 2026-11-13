def a(x: int) -> None: 
 print(x*2)
 
def b(x: int) -> int:
    return x*2

resultadoa= a(5)
resultadob= b(5)

print(f"{resultadoa}") #devuelve NONE, no hemos puesto return
print(f"{resultadob}")