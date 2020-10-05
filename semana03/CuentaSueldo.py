from Cuenta import Cuenta

class CuentaSueldo(Cuenta):

    # FIXME: titular debe ser un cliente
    def __init__(self, numero = "2", cliente = "Lucas", empleador = "Fabian", cuit_empleador = "23-12345678-1"):
        Cuenta.__init__(self, numero, cliente)
        self._empleador = empleador
        self._cuit_empleador = cuit_empleador
        self._extracciones_permitidas = 10
        self._extracciones_realizadas = 3

    def __str__(self):
        return f"Cuenta: {self._numero} \nTitular: {self._titular} \nEmpleador: {self._empleador} \nCUIT: {self._cuit_empleador}"

    def incrementar_extracciones_realizadas(incremento):
        pass

    def reset_extracciones_realizadas():
        pass

    def extraer(dinero):
        pass
