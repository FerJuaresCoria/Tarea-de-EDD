class Asistente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.eventos_anotados = []

    def agregar_a_evento(self, evento_a_agregar):
        if len(self.eventos_anotados) != 0:
            for evento in self.eventos_anotados:
                if evento.horario.horario_compatible(evento_a_agregar.horario):
                    continue
                else:
                    return False
        self.eventos_anotados.append(evento_a_agregar)
        return True
