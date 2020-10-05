class Conjunto():

    def __init__(self, inicio):
        self.lista = inicio

    def union(self , otra_lista):
        return [i for i in self.lista if i != otra_lista.lista] + [i for i in otra_lista.lista if i not in self.lista]

    def interseccion(self , otra_lista):
        return [i for i in self.lista if i in otra_lista.lista]

    def diferencia(self , otra_lista):
        return [i for i in self.lista if i not in otra_lista.lista]

    def diferencia_simetrica(self ,otra_lista):
        return [i for i in self.lista if i not in otra_lista.lista] + [i for i in otra_lista.lista if i not in self.lista]
