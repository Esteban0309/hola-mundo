#importamos el modulo math para asi poder calcular el area del circulo utilizando la constante pi.
import math

# Utilizamos una funcion para calcular el area del circulo, utilizando la formula a=math.pi*(r**2)
def calcular_area(radio):
    area = math.pi * (radio ** 2)
    return area
# Solicitamos al usuario que ingrese el radio del circulo.
radio = int(input("Ingrese el radio del círculo: "))
area = calcular_area(radio)
# Imprimimos el area del circulo
print(f"El área del círculo es: {area:.2f}")