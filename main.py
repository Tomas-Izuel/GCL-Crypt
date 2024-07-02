# main.py
from datetime import datetime
import time
import tkinter as tk
from encriptador.generador_congruencial import generar_parametros_desde_clave, generador_congruencial_lineal
from encriptador.normalizacion import normalizar
from encriptador.encriptador import encriptar_mensaje
from encriptador.pruebas import run_tests
from encriptador.utilidades import nombres_claves


def generar_clave():
    fecha_actual = datetime.now()
    a = fecha_actual.hour
    c = fecha_actual.minute
    semilla = int(time.time())
    secuencia_prueba = generador_congruencial_lineal(a, c, 2**32, semilla, 300)
    resultados_tests = run_tests(normalizar(secuencia_prueba, 2**32))
    clave_compartida = nombres_claves[tuple(resultados_tests)]
    return clave_compartida


def obtener_random_numbers(clave_compartida, n=100):
    a, c, m, seed = generar_parametros_desde_clave(clave_compartida)
    random_numbers = generador_congruencial_lineal(a, c, m, seed, n)
    random_numbers_normalizados = normalizar(random_numbers, m)
    return random_numbers_normalizados


def encriptar():
    mensaje = entry_mensaje.get()
    random_numbers_normalizados = obtener_random_numbers(clave)
    mensaje_encriptado = encriptar_mensaje(mensaje, random_numbers_normalizados)
    entry_encriptado.delete(0, tk.END)
    entry_encriptado.insert(0, mensaje_encriptado)


def desencriptar():
    mensaje_encriptado = entry_encriptado.get()
    random_numbers_normalizados = obtener_random_numbers(clave)
    mensaje_desencriptado = encriptar_mensaje(mensaje_encriptado, random_numbers_normalizados)
    entry_desencriptado.delete(0, tk.END)
    entry_desencriptado.insert(0, mensaje_desencriptado)


clave = generar_clave()

root = tk.Tk()
root.title("Encriptador")

tk.Label(root, text="Mensaje:").grid(row=0, column=0)
entry_mensaje = tk.Entry(root, width=50)
entry_mensaje.grid(row=0, column=1)

tk.Label(root, text="Mensaje Encriptado:").grid(row=1, column=0)
entry_encriptado = tk.Entry(root, width=50)
entry_encriptado.grid(row=1, column=1)

tk.Label(root, text="Mensaje Desencriptado:").grid(row=2, column=0)
entry_desencriptado = tk.Entry(root, width=50)
entry_desencriptado.grid(row=2, column=1)

btn_encriptar = tk.Button(root, text="Encriptar", command=encriptar)
btn_encriptar.grid(row=3, column=0, columnspan=2)

btn_desencriptar = tk.Button(root, text="Desencriptar", command=desencriptar)
btn_desencriptar.grid(row=4, column=0, columnspan=2)

root.mainloop()
