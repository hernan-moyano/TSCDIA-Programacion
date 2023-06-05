#Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente.
numero = int(input("Ingrese un número del 1 al 7: "))

if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Lunes")
elif numero == 3:
    print("Martes")
elif numero == 4:
    print("Miércoles")
elif numero == 5:
    print("Jueves")
elif numero == 6:
    print("Viernes")
elif numero == 7:
    print("Sábado")
else:
    print("Número no válido. Por favor, ingrese un número del 1 al 7.")
