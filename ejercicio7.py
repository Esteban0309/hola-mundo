
# Utilizamos una funcion, para calcular la temperatura en grados Fahrenheit utilizando la fórmula F = (C × 9/5) + 32
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
# Solicitamos al usuario ingrese ls temperatura en grados Celsius
celsius = int(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
# Solicitamos al usuario imprimir la temperaturan en grados fahrenheit.
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}")
     