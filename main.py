# main.py
from encriptador.generador_congruencial import generar_parametros_desde_clave, generador_congruencial_lineal
from encriptador.normalizacion import normalizar
from encriptador.encriptador import encriptar_mensaje
from encriptador.pruebas import run_tests
from encriptador.utilidades import nombres_claves
import pyperclip


# Generar parámetros del GCL a partir de la clave
secuencia_prueba = generador_congruencial_lineal(1664525, 1013904223, 2**32, 123456789, 1000)
resultados_tests = run_tests(normalizar(secuencia_prueba, 2**32))

clave_compartida = nombres_claves[tuple(resultados_tests)]
print("Clave generada:", clave_compartida)

n = 100  # Longitud del mensaje

def encriptar(clave_compartida):
    a, c, m, seed = generar_parametros_desde_clave(clave_compartida)

    # Generar números pseudoaleatorios
    random_numbers = generador_congruencial_lineal(a, c, m, seed, n)

    # Normalizar números
    random_numbers_normalizados = normalizar(random_numbers, m)

    opcion = input("Escriba el mensaje a encriptar: ")
    # Mensaje a encriptar
    mensaje = opcion

    # Encriptar el mensaje
    mensaje_encriptado = encriptar_mensaje(mensaje, random_numbers_normalizados)
    print("Mensaje encriptado:", mensaje_encriptado, "\n")
    pyperclip.copy(mensaje_encriptado)
    print("El mensaje fue copiado en el portapapeles.")

def desencriptar(clave_compartida, mensaje_encriptado):
    # Para desencriptar el mensaje (usando la misma clave)
    a, c, m, seed = generar_parametros_desde_clave(clave_compartida)
    random_numbers = generador_congruencial_lineal(a, c, m, seed, n)
    random_numbers_normalizados = normalizar(random_numbers, m)
    mensaje_desencriptado = encriptar_mensaje(mensaje_encriptado, random_numbers_normalizados)
    print("Mensaje desencriptado:", mensaje_desencriptado)

def main():
    opcion = input("Escriba 'encriptar' o 'desencriptar': ")
    if opcion == 'encriptar':
        encriptar(clave_compartida)
    elif opcion == 'desencriptar':
        mensaje_encriptado = input("Escriba el mensaje encriptado: ")
        desencriptar(clave_compartida, pyperclip.paste())
    else:
        print("Opción no válida")

if __name__ == '__main__':
    main()