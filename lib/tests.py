# tests.py
from math import expm1
import numpy as np
from scipy.stats import chisquare, kstest, norm
from collections import Counter

def run_tests(secuencia):
    resultados_tests = []

    # Test de Chi Cuadrada
    chi_pvalue = chi_cuadrada_test(secuencia)
    if chi_pvalue >= 0.05:
        resultados_tests.append(1)
    else:
        resultados_tests.append(0)

    # Test de Kolmogorov-Smirnov
    ks_pvalue = ks_test(secuencia)
    if ks_pvalue >= 0.05:
        resultados_tests.append(1)
    else:
        resultados_tests.append(0)

    # Test de Rachas
    rachas_pvalue = rachas_test(secuencia)
    if rachas_pvalue >= 0.05:
        resultados_tests.append(1)
    else:
        resultados_tests.append(0)

    # Test de Poker
    poker_pvalue = poker_test(secuencia)
    if poker_pvalue >= 0.05:
        resultados_tests.append(1)
    else:
        resultados_tests.append(0)

    return resultados_tests

def chi_cuadrada_test(secuencia):
    observados, _ = np.histogram(secuencia, bins=10)
    expected = np.ones_like(observados) * len(secuencia) / 10
    _, pvalue = chisquare(observados, f_exp=expected)
    return pvalue

def ks_test(secuencia):
    _, pvalue = kstest(secuencia, 'uniform')
    return pvalue

def rachas_test(secuencia):
    n = len(secuencia)
    mediana = np.median(secuencia)
    rachas = [1 if x >= mediana else 0 for x in secuencia]
    
    num_rachas = sum(1 for _ in range(n - 1) if rachas[_] != rachas[_ + 1]) + 1
    mean_rachas = (2 * n - 1) / 3
    std_rachas = np.sqrt((16 * n - 29) / 90)
    
    z = (num_rachas - mean_rachas) / std_rachas
    pvalue = 2 * (1 - norm.cdf(abs(z)))
    
    return pvalue

def poker_test(secuencia):
    n = len(secuencia)
    frecuencias = Counter(int(x * 10) for x in secuencia)
    
    f_i = [frecuencias[i] for i in range(10)]
    g = sum(f_i[i]**2 for i in range(10))
    
    poker = (16 / 5000) * g - 5000
    # Uso de expm1 para evitar overflow
    if poker < 0:
        pvalue = -expm1(poker)
    else:
        pvalue = 1 - np.exp(-poker)
    
    return pvalue
