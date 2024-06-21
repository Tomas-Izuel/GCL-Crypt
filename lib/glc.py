
class GeneradorCongruencialLineal:
    def __init__(self, mensaje):
        self.mensaje = mensaje
        self.longitud = len(mensaje)
        self.modulo = self.longitud
        self.incremento = self.get_incremento()
        self.multiplicador = self.get_multiplicador()

    def get_incremento(self):
        # Encontrar el último número primo que divide al módulo
        for i in range(self.modulo, 1, -1):
            if self.modulo % i == 0:
                primo = True
                for j in range(2, i):
                    if i % j == 0:
                        primo = False
                if primo:
                    return i

    def get_multiplicador(self):
        # Encontrar el primer número primo que divide a un número distinto de 1
        uno = 1
        for k in range(2, self.modulo):
            if uno % k == 0:
                primo2 = True
                for l in range(2, k):
                    if k % l == 0:
                        primo2 = False
                if primo2:
                    return k

    def generar_secuencia(self):
        # Generar secuencia de números pseudoaleatorios usando GCL
        secuencia = []
        semilla = 2
        for _ in range(self.longitud):
            semilla = (self.multiplicador * semilla + self.incremento) % self.modulo
            secuencia.append(semilla / self.modulo)  # Genera número tipo 0.xxx
        return secuencia