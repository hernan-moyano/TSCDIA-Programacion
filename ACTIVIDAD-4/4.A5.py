#Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo
#el cambio de dólares a pesos y que sea el usuario quién decida qué tipo
#de cambio quiere, si de dólares a pesos o viceversa.

tasa_cambio = float(input("Ingrese la cotización para el tipo de cambio vendedor: "))
opcion = input("Seleccione la dirección de conversión (1 - Pesos a Dólares, 2 - Dólares a Pesos): ")

if opcion == "1":
    pesos = float(input("Ingrese la cantidad de pesos: "))
    dolares = pesos / tasa_cambio
    print(f"{pesos} pesos equivale a {dolares} dólares.")
elif opcion == "2":
    dolares = float(input("Ingrese la cantidad de dólares: "))
    pesos = dolares * tasa_cambio
    print(f"{dolares} dólares equivale a {pesos} pesos.")
else:
    print("Opción no válida.")
