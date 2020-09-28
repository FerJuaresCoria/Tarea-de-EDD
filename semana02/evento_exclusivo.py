from evento import Evento

class Evento_exclusivo(Evento):
    def __init__(self, nombre, inicio, fin, cupos):
        Evento.__init__(self, nombre, inicio, fin)
        self.cupos = cupos
