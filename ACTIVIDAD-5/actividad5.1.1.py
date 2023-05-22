print("Ciclo repetitivo WHILE con listas de números")
x=1
while x<11:
    print(x)
    x+=1 #x=x+1
print("Fin del bucle o ciclo")
# While con cadena de caracteres
print("\n Ciclo repetitivo WHILE con cadena de caracteres\n")
x=1
while x<6:
    print(x ,"Programación I")
    x+=1
print("Fin del bucle o ciclo")

# FOR con elementos (range, list)
print("\n Ciclo repetitivo FOR con listas de números y elemento range\n")
for a in range(11):
    print(a)
# FOR con elementos (range con inicio y fin)
print("\n Ciclo repetitivo FOR con listas de números y elemento range con valor inicial y valor final\n")
for a in range(100,151):
    print(a)
print("Fin del bucle o ciclo")   
# FOR con elementos (range con inicio, fin y estableciendo uns estructura: tabla de 5 )
print("\n Ciclo repetitivo FOR con listas de números y elemento range con valor inicial,valor final e impar\n")
for a in range(0,26,5):
    print(a)
print("Fin del bucle o ciclo")

 # FOR con elementos (list con palabras )
print("\n Ciclo repetitivo FOR con listas de palabras \n")
for b in ["primavera","verano","otoño","invierno"]:
    print("Hola a todas las estaciones del año!")
   
# FOR con elementos (list con palabras )
print("\n Ciclo repetitivo FOR con listas de palabras \n")
for estacion in ["primavera","verano","otoño","invierno"]:
    print("Hola, estación: ", estacion)

# FOR con elementos (list con números )
print("\n Ciclo repetitivo FOR con listas de números \n")
for c in [1,2,3,4,5,6,7,8,9]:
    print(c,"- Hola a tod@s!")

# FOR con elementos (list con números )
print("\n Ciclo repetitivo FOR con listas de números \n")
for d in [1,2,3,4,5,6,7,8,9,10]:
    print("Esta es la iteración N°:", d)
