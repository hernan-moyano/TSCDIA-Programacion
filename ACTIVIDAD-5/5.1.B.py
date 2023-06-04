# Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.

numeros = []  # Lista para almacenar los números ingresados
contador = 0  # Contador de números ingresados

# Leer 10 números
while contador < 10:
    numero = int(input("Ingresa un número: "))
    numeros.append(numero)
    contador += 1

# Contar cantidad de números mayores y menores a 100
mayores_a_100 = 0
menores_a_100 = 0
indice = 0

while indice < len(numeros):
    if numeros[indice] > 100:
        mayores_a_100 += 1
    elif numeros[indice] < 100:
        menores_a_100 += 1
    indice += 1

# Obtener número máximo y mínimo
numero_maximo = max(numeros)
numero_minimo = min(numeros)

# Imprimir resultados
print("Cantidad de números mayores a 100:", mayores_a_100)
print("Cantidad de números menores a 100:", menores_a_100)
print("Número máximo:", numero_maximo)
print("Número mínimo:", numero_minimo)
