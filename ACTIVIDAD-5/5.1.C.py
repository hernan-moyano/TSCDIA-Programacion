#Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, 
#cuántos mayores de edad y cuántos menores de edad.

# Variables para contar las cantidades
cantidad_mujeres = 0
cantidad_varones = 0
cantidad_mayores = 0
cantidad_menores = 0

# Bucle para ingresar los datos de las personas
for i in range(15):
    print(f"\nPersona {i+1}:")
    
    # Ingresar el sexo de la persona (M o F)
    sexo = input("Sexo (M/F): ").upper()
    
    # Verificar si es hombre o mujer
    if sexo == "M":
        cantidad_varones += 1
    elif sexo == "F":
        cantidad_mujeres += 1
    else:
        print("Sexo inválido. Se considerará como masculino.")
        cantidad_varones += 1
    
    # Ingresar la edad de la persona
    edad = int(input("Edad: "))
    
    # Verificar si es mayor o menor de edad
    if edad >= 18:
        cantidad_mayores += 1
    else:
        cantidad_menores += 1

# Imprimir los resultados
print("\nResultados:")
print("Cantidad de mujeres:", cantidad_mujeres)
print("Cantidad de varones:", cantidad_varones)
print("Cantidad de mayores de edad:", cantidad_mayores)
print("Cantidad de menores de edad:", cantidad_menores)
