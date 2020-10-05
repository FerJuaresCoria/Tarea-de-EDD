class Cliente(object):

    def __init__(self, nombre = "nombre generico", dni = "12345678"):
        self._nombre = nombre
        self._dni = dni

    def __str__(self):
        return f"Nombre: {self._nombre} \nDNI: {self._dni}"

    def enviar_mensaje(mensaje):
        pass
