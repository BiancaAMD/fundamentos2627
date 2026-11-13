import math
unidades: int = 47
cantidadPorCaja: int = 10

cajas: int = math.ceil(unidades/cantidadPorCaja)
print(f"Para {unidades} unidades, necesitarías {cajas} cajas")