'''
def procesar(notas):
    m = sum(notas) / len(notas)
    print(f"Media: {m:.2f}")
'''

def media(notas: list [float])-> float:
    return sum(notas)/len(notas)


def mostrarMedia(notas: list[float]) -> None:
    print(f"La media es: {media(notas):.2f}")
    

if __name__ == "__main__":
    mostrarMedia([5,5,5,5])
