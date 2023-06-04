#Leer 10 números y mostrar solamente los números positivos, y su sumatoria.

numeros = []  # Lista para almacenar los números ingresados
sumatoria = 0  # Variable para almacenar la sumatoria de los números positivos

# Leer los 10 números
for i in range(10):
    numero = float(input("Ingrese el número {}: ".format(i + 1)))
    numeros.append(numero)

# Mostrar los números positivos y calcular la sumatoria
for numero in numeros:
    if numero > 0:
        print(numero)
        sumatoria += numero

print("La sumatoria de los números positivos es:", sumatoria)
