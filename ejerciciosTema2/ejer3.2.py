def saludar(nombre: str, saludo: str = "Hola") -> str: #valor por defecto en saludo
    return f"{saludo}, {nombre}"

print(saludar("Bianca", "Bienvenida"))