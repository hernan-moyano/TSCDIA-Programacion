#Realizar un programa que permita ingresar “f” o “m” y determinar si vota en mesa femenina o masculina.
genero = input("Ingrese su género (f/m): ")

if genero.lower() == "f":
    print("Vota en mesa femenina.")
elif genero.lower() == "m":
    print("Vota en mesa masculina.")
else:
    print("Género no válido.")
