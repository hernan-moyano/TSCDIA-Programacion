# Realice un programa que le permita al usuario simular el pago
# ingresando el importe y la forma de pago:
# • Contado (1): se aplica un descuento del 10% al importe
# • Tarjeta (2): se aplica un interés de 10%
# • Débito (3): se aplica un descuento del 5%
# Mostrar el importe, el descuento o interés y el importe total.
importe = float(input("Ingrese el importe a pagar: "))
forma_pago = int(input("Seleccione la forma de pago (1 - Contado, 2 - Tarjeta, 3 - Débito): "))

if forma_pago == 1:
    descuento = importe * 0.1
    importe_total = importe - descuento
    print(f"Importe: ${importe}")
    print(f"Descuento: ${descuento}")
    print(f"Importe total: ${importe_total}")
elif forma_pago == 2:
    interes = importe * 0.1
    importe_total = importe + interes
    print(f"Importe: ${importe}")
    print(f"Interés: ${interes}")
    print(f"Importe total: ${importe_total}")
elif forma_pago == 3:
    descuento = importe * 0.05
    importe_total = importe - descuento
    print(f"Importe: ${importe}")
    print(f"Descuento: ${descuento}")
    print(f"Importe total: ${importe_total}")
else:
    print("Forma de pago no válida.")
