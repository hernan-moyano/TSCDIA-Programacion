#Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente.
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

numero = int(input("Ingrese un número del 1 al 12: "))

if numero >= 1 and numero <= 12:
    nombre_mes = meses[numero - 1]
    print(f"El mes correspondiente al número {numero} es {nombre_mes}.")
else:
    print("Número no válido. Por favor, ingrese un número del 1 al 12.")
