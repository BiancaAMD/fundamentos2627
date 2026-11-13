def hacerMedia(notas: list[float]) -> float:
    
    return sum(notas)/len(notas)
    
def redondear(media: float)-> int:
    return round(media)

def aprobado(media: int)-> bool:
    return media>=5
    
if __name__ == "__main__":
    media = hacerMedia({1,1,1,1,1})
    mediaRedondeada = redondear(media)
    
    print(f"Media: {media}")
    print(f"Media redondeada: {mediaRedondeada}")
    print(f"El alumno aprueba: {aprobado(mediaRedondeada)}")
          
          
        