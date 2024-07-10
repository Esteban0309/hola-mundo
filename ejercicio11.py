limite = int(input("Introduce un número límite: "))
suma = 0
for i in range(1, limite + 1):
    suma += i
print(f"La suma de todos los números naturales hasta {limite} es {suma}")