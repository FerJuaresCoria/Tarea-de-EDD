from CuentaSueldo import CuentaSueldo

class CuentaSueldoPlus(CuentaSueldo):

    # FIXME: titular debe ser un cliente
    def __init__(self, numero = "4", cliente = "Martin", empleador = "Fabian", cuit_empleador = "20-12345678-6"):
        CuentaSueldo.__init__(self, numero, cliente, empleador, cuit_empleador)
        self._descubierto = 1500.0

    def __str__(self):
        return f"Cuenta: {self.numero} \nTitular: {self.titular} \nEmpleador: {self.empleador} \nCUIT: {self.cuit_empleador} \nDescubierto: {self.descubierto}"

    def set_cantidad_extracciones():
        pass

    def obtener_disponible():
        pass

    def aviso_descubierto():
        pass

    def set_descubierto():
        pass

    def get_descubierto():
        pass
