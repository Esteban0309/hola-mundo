# Solicitamos al usuario ingresar su peso y altura
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))
# Escribimos la formula a utilizar
imc = peso / (altura ** 2)
#Clasificamos el imc
if imc < 18.5:
    clasificacion = "Bajo peso"
elif imc < 25:
    clasificacion = "Peso normal"
elif imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"
# Mostramos el resultado dependiendo el peso y altura del usuario
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")
print(f"Tu clasificación es: {clasificacion}")