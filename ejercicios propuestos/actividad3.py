total: int = int(input("Segundos: "))

horas: int = total // 3600
minutos: int = (total % 3600) // 60
seg: int = total % 60

print(f"{horas}h {minutos}m {seg}s")  