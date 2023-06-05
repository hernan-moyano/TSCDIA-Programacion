#Realice un programa que lea dos números y diga cuál es el mayor.
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if numero1 > numero2:
    print("El primer número es mayor.")
elif numero2 > numero1:
    print("El segundo número es mayor.")
else:
    print("Ambos números son iguales.")
