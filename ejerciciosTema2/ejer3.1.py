def presentar(nombre: str , ciudad: str) -> str:
    return f"Te llamas {nombre} y vives en {ciudad}"

#posición
print(presentar("Bianca", "Alcalá"))

#nombre, orden da igual
print(presentar(ciudad="Alcalá", nombre="Bianca"))