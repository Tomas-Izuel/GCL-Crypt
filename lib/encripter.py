# encripter.py

def encriptar_mensaje(secuencia, mensaje, resultados_tests):
    mensaje_encriptado = []
    multiplicador = convertir_binario_a_decimal(resultados_tests)
    
    for i in range(len(mensaje)):
        valor_encriptado = int(secuencia[i]) + ord(mensaje[i]) * multiplicador
        # Asegurarse de que el valor encriptado se mantenga en el rango de valores de caracteres ASCII válidos
        while valor_encriptado > 255:
            valor_encriptado -= 255
        mensaje_encriptado.append(chr(valor_encriptado))
    
    # Unir la lista en una cadena antes de devolver
    return ''.join(mensaje_encriptado) + chr((multiplicador))

def convertir_binario_a_decimal(binario):
    decimal = 1
    for i in range(len(binario)):
        decimal += binario[i] * 2**(len(binario) - 1 - i)
    return decimal

