def convertir_decimal(decimal):
    binario = bin(decimal)[2:]  # Convertir a binario y omitir los dos primeros caracteres '0b'
    hexadecimal = hex(decimal)[2:]  # Convertir a hexadecimal y omitir los dos primeros caracteres '0x'
    
    print("El número decimal", decimal, "convertido a binario es:", binario)
    print("El número decimal", decimal, "convertido a hexadecimal es:", hexadecimal)

#Uso
convertir_decimal(9)