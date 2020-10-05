from Cuenta import Cuenta

class CuentaMultipersona(Cuenta):

    # FIXME: titulares debe ser una lista de clientes
    def __init__(self, numero = "450318893665", titulares = ["Lucas", "Aaron"]):
        Cuenta.__init__(self)
        self._numero = "3"
        self._titulares = titulares

    def __str__(self):
        return "Cuenta : " + self._numero + "\nTitulares: " + str([titular for titular in self._titulares])

    def agregar_titular(titular):
        pass

    def get_descubierto():
        pass

    def obtener_disponible():
        pass

    def aviso_descubierto():
        pass

    def set_descubierto():
        pass
