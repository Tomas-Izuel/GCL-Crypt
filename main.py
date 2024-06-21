

from lib.encripter import encriptar_mensaje
from lib.glc import GeneradorCongruencialLineal
from lib.tests import run_tests


def main():
    mensaje = input("Ingrese el mensaje a encriptar: ")
    
    # Paso 1: Generar secuencia de números pseudoaleatorios con GCL
    generador = GeneradorCongruencialLineal(mensaje)
    secuencia = generador.generar_secuencia()
    
    # Paso 2: Ejecutar tests de aleatoriedad
    resultados_tests = run_tests(secuencia)
    
    # Paso 3: Encriptar el mensaje original
    mensaje_encriptado = encriptar_mensaje(mensaje, resultados_tests)
    
    print("Mensaje encriptado:", mensaje_encriptado)

if __name__ == "__main__":
    main()
