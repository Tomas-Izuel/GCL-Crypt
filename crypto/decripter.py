def convertir_hexa_a_tests_decimal(hexa_tests):
    tests_binario = bytes.fromhex(hexa_tests).decode('utf-8')
    return ord(tests_binario)

def convertir_binario_a_decimal(binario):
    decimal = 1
    for i in range(len(binario)):
        decimal += binario[i] * 2**(len(binario) - 1 - i)
    return decimal

def desencriptar_mensaje(mensaje_encriptado, secuencia, resultados_tests):
    mensaje_desencriptado = []
    test_binario = convertir_binario_a_decimal(resultados_tests)
    test_decimal = convertir_hexa_a_tests_decimal(test_binario)
    
    for i, letra in enumerate(mensaje_encriptado.split()[:-1]):
        hexa_letra_encriptada = int(letra, 16)
        ascii_letra = hexa_letra_encriptada - int(secuencia[i] * 100) - test_decimal
        letra_desencriptada = chr(ascii_letra)
        mensaje_desencriptado.append(letra_desencriptada)
    
    return ''.join(mensaje_desencriptado)