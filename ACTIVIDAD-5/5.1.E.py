# Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.

numeros_negativos = 0
numeros_convertidos = []

while numeros_negativos < 15:
    numero = int(input("Ingrese un número: "))
    if numero < 0:
        numeros_negativos += 1
        numero = abs(numero)  # Convertir el número a positivo
        numeros_convertidos.append(numero)

print("Los números convertidos a positivos son:")
for numero in numeros_convertidos:
    print(numero)
