def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    total = cantidad_sin_iva + cantidad_sin_iva * (porcentaje_iva / 100)
    return print(f"El importe sin IVA es: ${cantidad_sin_iva}, con IVA al {porcentaje_iva}% es: ${total}\n" )

#Uso
calcular_total_factura(1000)
calcular_total_factura(1000,15)