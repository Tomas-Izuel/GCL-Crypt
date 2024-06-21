def encriptar_mensaje(mensaje, resultados_tests):
    indice_test = sum(resultados_tests)  # Calcular el índice según los resultados de los tests
    multiplicador = 10 ** len(str(ord('A')))  # Multiplicador para ajustar a dígitos ASCII
    mensaje_encriptado = []
    
    for i, letra in enumerate(mensaje):
        num_aleatorio = resultados_tests[i] * multiplicador
        valor_ascii = ord(letra)
        valor_encriptado = int(num_aleatorio) + valor_ascii + indice_test
        mensaje_encriptado.append(chr(valor_encriptado))
    
    return ''.join(mensaje_encriptado)
