from horario import Horario

class Evento:
    def __init__(self, nombre, inicio, fin):
        self.nombre = nombre
        self.horario = Horario(inicio, fin)
        self.espectadores = 0
