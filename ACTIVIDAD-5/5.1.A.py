# Realice un programa que lea 4 numeros y diga cuantos son pares y cuantos impares y devuelva la sumatoria de los pares.

numeros = []
pares = 0
sumatoria_pares = 0

for i in range(4):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

    if num % 2 == 0:
        pares += 1
        sumatoria_pares += num

impares = 4 - pares

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Sumatoria de los números pares:", sumatoria_pares)
