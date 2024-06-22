# encriptador.py
from .generador_congruencial import generar_parametros_desde_clave, generador_congruencial_lineal
from .normalizacion import normalizar

def encriptar_mensaje(mensaje, random_numbers):
    encriptado = []
    for i, char in enumerate(mensaje):
        key = int(random_numbers[i] * 255)  # Convertimos el número aleatorio a un valor entre 0 y 255
        encriptado.append(chr(ord(char) ^ key))
    return ''.join(encriptado)
