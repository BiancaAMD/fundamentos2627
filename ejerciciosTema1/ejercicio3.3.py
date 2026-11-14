tiempo: int = 3725

horas: int = tiempo//3600
tiempo = tiempo%3600
minutos: int = tiempo//60
tiempo = tiempo%60
segundos: int = tiempo

print(f"{horas}h")
print(f"{minutos}m")
print(f"{segundos}s")
