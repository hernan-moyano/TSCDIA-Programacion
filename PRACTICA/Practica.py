def conversion(segundos):
    #60 seg * 60 min = 1 hora
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = (segundos % 3600) % 60
    return horas, minutos, segundos

segundos_totales = int(input("Por favor, ingresar el número total de segundos: "))
horas, minutos, segundos = conversion(segundos_totales)
print(f"Los segundos ingresados equivalen a: {horas} horas, {minutos} minutos, {segundos} segundos. Muchas gracias por su consulta!.")
