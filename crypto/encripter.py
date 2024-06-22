# encripter.py

def encriptar_mensaje(secuencia, mensaje, tests):
    
    mensaje_encriptado = []
    test_binario = convertir_binario_a_decimal(tests)

    for i, letra in enumerate(mensaje):
        ascii_letra = ord(letra)
        hexa_letra_encriptada = int(secuencia[i] * 100) + ascii_letra + test_binario
        # Convertir el número en hexadecimal de 1 byte (dos caracteres)
        hexa_en_byte = format(hexa_letra_encriptada, '02X')
        mensaje_encriptado.append(hexa_en_byte)

    return ' '.join(mensaje_encriptado)

def convertir_binario_a_decimal(binario):
    decimal = 1
    for i in range(len(binario)):
        decimal += binario[i] * 2**(len(binario) - 1 - i)
    return decimal
