x: int = 10
def f() -> None:
    x = 99
    print(x) #imprime local
    
f()
print(x) #imprime global