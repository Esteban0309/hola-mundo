# Solicitamo al usuario ingrese uan cadena de texto
cadena = input("Introduce una cadena: ")
# Definimos una variable que contenga las vocales mayusculas y minusculas
vocales = "aeiouAEIOU"
contador_vocales = 0
# Utilizamos un bucle que me ayude a contar las vocales
for caracter in cadena:
    if caracter in vocales:
        contador_vocales += 1
# Imprimimos la cantidad de vocales que tiene la cadena de texto ingresada anteriormente
print(f"La cadena tiene {contador_vocales} vocales")