# -*- coding: utf-8 -*-
from crypto.decripter import desencriptar_mensaje
from crypto.encripter import encriptar_mensaje
from lib.glc import GeneradorCongruencialLineal
from lib.tests import run_tests

def main():
    while True:
        print("\nMenú:")
        print("1. Encriptar mensaje")
        print("2. Desencriptar mensaje")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mensaje = input("Ingrese el mensaje a encriptar: ")
            
            longitud = len(mensaje)
            generador = GeneradorCongruencialLineal(longitud)
            secuencia = generador.generar_secuencia()
            test = run_tests(secuencia)
            print("Tests:", test)

            print("\n")

            mensaje_encriptado = encriptar_mensaje(secuencia, mensaje, test)
            print("Mensaje encriptado:", mensaje_encriptado)
            
        
        elif opcion == "2":
            mensaje_encriptado = input("Ingrese el mensaje encriptado: ")
            
            longitud = len(mensaje_encriptado) - 1
            generador = GeneradorCongruencialLineal(longitud)
            secuencia = generador.generar_secuencia()
            test = run_tests(secuencia)
            print("Tests:", test)

            print("\n")

            mensaje_desencriptado = desencriptar_mensaje(mensaje_encriptado, secuencia, test)
            print("Mensaje desencriptado:", mensaje_desencriptado)
        
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()
