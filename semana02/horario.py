class Horario:
    def __init__(self, inicio, fin):
        self.horario_inicio = inicio
        self.horario_fin = fin

    def horario_compatible(self, otro_horario):
        return (self.horario_inicio >= otro_horario.horario_fin or self.horario_fin <= otro_horario.horario_inicio)
