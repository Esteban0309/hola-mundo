# Pedimos al usuario que ingrese un número
numero = int(input("Ingrese un número: "))
# Creamos un bucle que sea desde 1 hasta 12, es decir, los numeros por los que queremos que se realice la multiplicacion.
for i in range(1, 13):
# Calculamos la respuesta de la multiplicación
    producto = numero * i
# Imprimimos la operación y el resultado
    print(f"{numero} x {i} = {producto}")