# main.py
from datetime import datetime
import time
from encriptador.generador_congruencial import generar_parametros_desde_clave, generador_congruencial_lineal
from encriptador.normalizacion import normalizar
from encriptador.encriptador import encriptar_mensaje
from encriptador.pruebas import run_tests
from encriptador.utilidades import nombres_claves


fecha_actual = datetime.now()
# Obtener valores para a y c basados en la fecha actual
a = fecha_actual.hour
c = fecha_actual.minute

# Obtener la fecha y hora actual como semilla para el generador
semilla = int(time.time())

# Generar parámetros del GCL a partir de la clave
secuencia_prueba = generador_congruencial_lineal(a, c, 2**32, semilla, 300)
resultados_tests = run_tests(normalizar(secuencia_prueba, 2**32))

print("Resultados de los tests:", resultados_tests)

clave_compartida = nombres_claves[tuple(resultados_tests)]
print("Clave generada:", clave_compartida)

a, c, m, seed = generar_parametros_desde_clave(clave_compartida)
n = 100  # Longitud del mensaje

# Generar números pseudoaleatorios
random_numbers = generador_congruencial_lineal(a, c, m, seed, n)

# Normalizar números
random_numbers_normalizados = normalizar(random_numbers, m)
print("Números pseudoaleatorios normalizados:", random_numbers_normalizados)

opcion = input("Escriba el mensaje a encriptar: ")
# Mensaje a encriptar
mensaje = opcion

# Encriptar el mensaje
mensaje_encriptado = encriptar_mensaje(mensaje, random_numbers_normalizados)
print("Mensaje encriptado:", mensaje_encriptado)

# Para desencriptar el mensaje (usando la misma clave)
a, c, m, seed = generar_parametros_desde_clave(clave_compartida)
random_numbers = generador_congruencial_lineal(a, c, m, seed, n)
random_numbers_normalizados = normalizar(random_numbers, m)
mensaje_desencriptado = encriptar_mensaje(mensaje_encriptado, random_numbers_normalizados)
print("Mensaje desencriptado:", mensaje_desencriptado)
