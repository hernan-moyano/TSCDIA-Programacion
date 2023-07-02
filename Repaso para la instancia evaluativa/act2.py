def decorador(funcion):
    def envoltorio():
        print("Antes de ejecutar la función decorada")
        funcion()
        print("Después de ejecutar la función decorada")
    return envoltorio

def funcion_principal():
    print("Esta es una funcion sin decorar")

@decorador
def funcion_decorada():
    for i in range(6):
        if i % 2 == 0:
            print(i, "es par")
        else:
            print(i, "es impar")

funcion_principal()
print("-------------------")
funcion_decorada()
