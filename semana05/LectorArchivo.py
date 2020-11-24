#-*- coding: utf-8 -*-
import string
import json

class LectorArchivo():

    def __init__(self, novela):
        self.novela = novela
        self.capitulos = {}

    def dividir_capitulos(self, capitulos, final):
        capitulos.append(final)
        fragmentos = {}
        indice = 0
        entro_en_capitulo = False
        with open(self.novela, encoding="utf8") as archivo:
            novela = archivo.readlines()
            for linea, valor in enumerate(novela):
                novela[linea] = valor.replace("--", " ")
                novela[linea] = novela[linea].replace("\n", " ")
                if novela[linea].find(capitulos[-1]) >= 0:
                    break
                if indice < len(capitulos) - 1:
                    if novela[linea].find(capitulos[indice + 1]) >= 0 and novela[linea].find("(p") >= 0:
                        entro_en_capitulo = False
                        indice += 1
                    if novela[linea].find(capitulos[indice]) >= 0 and novela[linea].find("(p") >= 0:
                        fragmentos[capitulos[indice]] = " "
                        entro_en_capitulo = True
                    if entro_en_capitulo:
                        fragmentos[capitulos[indice]] = fragmentos[capitulos[indice]] + novela[linea]
            self.almacenar_en_archivo(fragmentos)

    def almacenar_en_archivo(self, diccionario):
        for clave, valor in diccionario.items():
            with open(clave + ".txt", "w") as archivo_json:
                json.dump(valor, archivo_json)


if __name__ == '__main__':
    a = LectorArchivo("NOVELAS CORTAS.txt")
    final = "EPÍLOGO"
    caps = ["LA BUENAVENTURA", "LA CORNETA DE LLAVES", "LAS DOS GLORIAS", "EL AFRANCESADO", "¡VIVA EL PAPA!", "EL EXTRANJERO", "EL LIBRO TALONARIO","MOROS Y CRISTIANOS", "EL AÑO EN SPITZBERG"]
    a.dividir_capitulos(caps, final)
