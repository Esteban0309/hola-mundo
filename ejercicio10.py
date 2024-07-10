# Utilizamos una funcion y ponemos restricciones para saber si es primo o no
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# Solicitamos al usuario que ingrese un numero
numero = int(input("Introduce un número: "))
# Damos normas para imprimir si el numero es primo o no.
if es_primo(numero):
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")