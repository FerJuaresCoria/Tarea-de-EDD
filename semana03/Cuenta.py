class Cuenta:

    # FIXME: titular debe ser un Cliente
    def __init__(self, numero = "1", titular = "Lucas"):
        self._numero = numero
        self._saldo = 1000.0
        self._titular = titular

    def __str__(self):
        return f"Cuenta: {self._numero} \nTitular: {self._titular}"

    def depositar(dinero):
        pass

    def extraer(dinero):
        pass

'''
1 : cuenta
2 : cuenta sueldo
3 : cuenta multipersona
4 : cuenta sueldo plus
'''
