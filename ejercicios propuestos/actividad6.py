importe : int = int(input("Cantidad de céntimos: "))

print(f"Monedas 50: {importe//50}")

print(f"Monedad 20: {(importe%50)//20}")

print(f"Monedas 10: {((importe%50)%20)//10}")

print(f"Monedas 5: {(((importe%50)%20)%10)//5}")

print(f"Monedas 2: {((((importe%50)%20)%10)%5)//2}")

print(f"Monedas 2: {((((importe%50)%20)%10)%5)%2}")



