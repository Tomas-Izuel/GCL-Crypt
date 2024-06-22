

from lib.encripter import encriptar_mensaje
from lib.glc import GeneradorCongruencialLineal
from lib.tests import run_tests


def main():
    mensaje = input("Ingrese el mensaje a encriptar: ")
    
    # Paso 1: Generar secuencia de números pseudoaleatorios con GCL
    generador = GeneradorCongruencialLineal(mensaje)
    print("GLC:", generador.__dict__)
    secuencia = generador.generar_secuencia()
    print("Secuencia:", secuencia)
    
    # Paso 2: Ejecutar tests de aleatoriedad
    resultados_tests = run_tests(secuencia)
    print("Resultados de tests:", resultados_tests)
    
    # Paso 3: Encriptar el mensaje original
    mensaje_encriptado = encriptar_mensaje(secuencia, mensaje, resultados_tests)
    
    print("Mensaje encriptado:", mensaje_encriptado)

if __name__ == "__main__":
    main()
