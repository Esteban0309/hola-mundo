def suma (num1,num2):
  return num1 + num2

def resta (num1,num2):
  return num1 - num2

def multiplicacion (num1,num2):
  return num1 * num2

def dividir (num1,num2):
  return num1 / num2

num1 = int(input('ingrese un numero'))
num2 = int(input('ingrese otro numero'))

print("Seleccione la operación a realizar:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

operacion = input('Selecione una operacion(1,2,3,4): ')

if operacion == "1":
    print(f"La suma de {num1} y {num2} es {suma(num1, num2)}")
elif operacion == "2":
    print(f"La resta de {num1} y {num2} es {resta(num1, num2)}")
elif operacion == "3":
    print(f"La multiplicación de {num1} y {num2} es {multiplicacion(num1, num2)}")
elif operacion == "4":
    print(f"La división de {num1} y {num2} es {division(num1, num2)}")
else:
    print("Error: operación no válida")