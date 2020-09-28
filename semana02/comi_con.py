from evento import Evento
from evento_exclusivo import Evento_exclusivo
from asistente import Asistente

class ComiCon:

    def __init__(self, asistentes, eventos):
        self.asistentes = []
        for asistente in asistentes:
            self.asistentes.append(Asistente(asistente))
        self.eventos = eventos
        self.comicon = {}
        self.organizar_asistentes()
        self.mostrar_eventos_de_asistentes()
        print(self.comicon)

    def organizar_asistentes(self):
        for evento in self.eventos:
            asistentes_del_evento = []
            for asistente in self.asistentes:
                if isinstance(evento, Evento_exclusivo):
                    if evento.cupos == 0:
                        continue
                if (asistente.agregar_a_evento(evento)):
                    if isinstance(evento, Evento_exclusivo):
                        evento.cupos -= 1
                    evento.espectadores += 1
                    asistentes_del_evento.append(asistente.nombre)
                    self.comicon[evento.nombre] = [asistentes_del_evento, evento.espectadores]

    def mostrar_eventos_de_asistentes(self):
        for asistente in self.asistentes:
            print(asistente.nombre, "tiene asignados los nombres de los siguientes eventos: ",  str([evento.nombre for evento in asistente.eventos_anotados]))

if __name__ == "__main__":
    asistentes = ["Luciano", "Julian", "Lucas", "Martín"]
    eventos = [Evento_exclusivo("Capitán América", 10, 13, 2),
        Evento_exclusivo("Hulk",10,11,1),
        Evento_exclusivo("Los 4 fantásticos",11,12,3),
        Evento_exclusivo("Mujer Maravilla",13,14,2),
        Evento("Hombre araña",16,17)]
    a = ComiCon(asistentes, eventos)
