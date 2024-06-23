# generador_congruencial.py
import hashlib

def generar_parametros_desde_clave(clave):
    # Usar una función hash (SHA-256) para generar parámetros pseudoaleatorios a partir de la clave
    hash_obj = hashlib.sha256(clave.encode())
    hash_digest = hash_obj.digest()
    
    # Convertir partes del hash en enteros para usarlos como parámetros del GCL
    a = int.from_bytes(hash_digest[:4], 'little')
    c = int.from_bytes(hash_digest[4:8], 'little')
    seed = int.from_bytes(hash_digest[8:12], 'little')
    
    # Ajustar los valores para que sean adecuados para el GCL
    m = 2**32
    a = a % m
    c = c % m
    seed = seed % m
    
    return a, c, m, seed

def generador_congruencial_lineal(a, b, m, seed, n):
    random_numbers = []
    X = seed
    for _ in range(n):
        X = (a * X + b) % m
        random_numbers.append(X)
    return random_numbers
