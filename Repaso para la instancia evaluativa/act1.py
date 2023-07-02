# Define la función decoradora para mostrar mensajes
def mostrar_mensaje(funcion):
    #Función que envuelve la función original con la funcionalidad adicional.
    def envoltura(*argumentos, **claveArgumentos):
        nombre_funcion = funcion.__name__.replace('_', ' ')
        print(f"\nRealizando cálculos para el {nombre_funcion}")
        resultado = funcion(*argumentos, **claveArgumentos)
        print(f"El área del {nombre_funcion} es: {resultado}\n")
    return envoltura

# Función decoradora para calcular el área del triángulo equilátero
@mostrar_mensaje
def triangulo_equilatero(lado):
    return (3**0.5 / 4) * lado**2

# Función decoradora para calcular el área del triángulo isósceles
@mostrar_mensaje
def triangulo_isosceles(base, altura):
    return (base * altura) / 2

# Función decoradora para triángulo escaleno
@mostrar_mensaje
def triangulo_escaleno(lado1, lado2, lado3):
    # Se utiliza la fórmula de Herón para calcular el área
    semiperimetro = (lado1 + lado2 + lado3) / 2
    return (semiperimetro * (semiperimetro - lado1) *
            (semiperimetro - lado2) * (semiperimetro - lado3)) ** 0.5

# Llamo a cada una de las funciones
triangulo_equilatero(3)
triangulo_isosceles(5, 3)
triangulo_escaleno(4, 3, 6)
