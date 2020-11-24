from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from LectorArchivo import LectorArchivo
import string

class IndiceInvertido():

    def __init__(self, documentos):
        self.spanish_stemmer = SnowballStemmer('spanish', ignore_stopwords=False)
        self.stop_words = frozenset(stopwords.words("spanish"))
        self.documentos = {}
        self.leer_textos(documentos)
        self.generar_documentos_a_identidicacion()
        self.generar_indice()

    def mostrar_stopwords(self):
        print(self.stop_words)

    def generar_documentos_a_identidicacion(self):
        self.documento_a_id={}
        docID = 0
        for documento in self.documentos.keys():
            self.documento_a_id[documento] = docID
            docID +=1
        self.id_a_documento = dict((value, key) for key, value in self.documento_a_id.items())

    def generar_indice(self):
        pares = []
        indice={}
        for documento in self.documentos:
            lista_palabras = [palabra for palabra in self.documentos[documento].split() if not palabra in self.stop_words]
            lista_palabras = [self.lematizar_palabra(palabra) for palabra in lista_palabras]
            pares= pares + [(palabra, self.documento_a_id[documento]) for palabra in lista_palabras]
        for par in pares:
            posting = indice.setdefault(par[0],set())
            posting.add(par[1])
        self.indice = indice

    def lematizar_palabra(self, palabra):
        palabra = palabra.strip(string.punctuation + "»" + "\x97" + "¿" + "¡" + "0123456789" + "«" + "[" + "]")
        palabra = palabra.rstrip("p")
        palabra_lematizada = self.spanish_stemmer.stem(palabra)
        return palabra_lematizada

    def leer_textos(self, textos):
        for texto in textos:
            with open(texto) as archivo:
                self.documentos[texto] = archivo.read()

    def buscar(self, palabra):
        salida=[]
        palabra_lematizada = self.lematizar_palabra(palabra)
        if palabra_lematizada in self.indice:
            for docID in self.indice[palabra_lematizada]:
                salida.append(self.id_a_documento[docID])
        return set(salida)


if __name__ == '__main__':
    palabras = ["vicario", "forastero", "parapeto", "tremebundo", "guillotina", "apellido", "caos", "entuerto", "suplicante", "continente"]
    documentos = ["LA BUENAVENTURA.txt", "LA CORNETA DE LLAVES.txt", "LAS DOS GLORIAS.txt", "EL AFRANCESADO.txt", "¡VIVA EL PAPA!.txt", "EL EXTRANJERO.txt", "EL LIBRO TALONARIO.txt","MOROS Y CRISTIANOS.txt", "EL AÑO EN SPITZBERG.txt"]
    a = IndiceInvertido(documentos)
    for palabra in palabras:
        print(a.buscar(palabra))
