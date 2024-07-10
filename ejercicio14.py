cadena = input("Introduce una cadena: ")

cadena_sin_espacios = cadena.replace(" ", "")

if cadena_sin_espacios == cadena_sin_espacios[::-1]:
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")