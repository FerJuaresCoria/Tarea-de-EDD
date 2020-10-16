#-*- coding: utf-8 -*-
#Registro del pais:
#https://datos.gob.ar/dataset/salud-covid-19-casos-registrados-republica-argentina/archivo/salud_fd657d02-a33a-498b-a91b-2ef1a68b8d16

import csv
import struct
import os
import operator

class EstadisticasCovid():

    def __init__(self, archivo):
        self.archivo = archivo
        self.edades = {"0-19" : 0, "20-39" : 0, "40-60" : 0, "+60" : 0}
        self.ranking = {}
        self.provincias = {}
        self.promedio_por_provincia = {}

    def casos_por_provincia(self, provincia, sexo):
        if provincia in self.provincias:
            #F = 0 / M = 1
            if sexo == "F":
                self.provincias[provincia][0] += 1
            else:
                self.provincias[provincia][1] = 1
        else:
            self.provincias[provincia] = [0, 0]
            self.casos_por_provincia(provincia, sexo)

    def casos_por_edad(self, edad, tipo_edad):
        if tipo_edad == ("Meses"):
            self.edades["0-19"] = self.edades["0-19"] + 1
        else:
            if int(edad) > 60:
                self.edades["+60"] = self.edades["+60"] + 1
            elif int(edad) <= 60 and int(edad) >= 40:
                self.edades["40-60"] = self.edades["40-60"] + 1
            elif int(edad) < 40 and int(edad) >= 20:
                self.edades["20-39"] = self.edades["20-39"] + 1
            elif int(edad) < 20:
                self.edades["0-19"] = self.edades["0-19"] + 1

    def agregar_al_promedio(self, provincia, edad, tipo_edad):
        if provincia in self.promedio_por_provincia:
            if tipo_edad == ("Meses"):
                self.promedio_por_provincia[provincia][0] += float(edad/12)
            else:
                self.promedio_por_provincia[provincia][0] += float(edad)
            self.promedio_por_provincia[provincia][1] += 1
        else:
            self.promedio_por_provincia[provincia] = [0.0, 0]
            self.agregar_al_promedio(provincia, edad, tipo_edad)

    def promediar_edad_por_provincia(self):
        promedio = {}
        for provincia, valores in self.promedio_por_provincia.items():
            promedio[provincia] = float(valores[0]/valores[1])
        return promedio

    def agregar_al_ranking(self, provincia):
        if provincia in self.ranking:
            self.ranking[provincia] = self.ranking[provincia] + 1
        else:
            self.ranking[provincia] = 1

    def almacenar_cantidad_de_casos_por_provincia(self):
        with open("cantidad_de_casos_por_provincia.txt", "wb") as datos:
            formato = "%ds%ds%ds" % (20, 7, 7)
            for provincia, sexo in self.provincias.items():
                datos.write(struct.pack(formato, provincia.encode(), str(sexo[0]).encode(), str(sexo[1]).encode()))

    def almacenar_casos_por_edad(self):
        with open("casos_por_edad.txt", "wb") as datos:
            formato = "%ds%ds" % (5, 7)
            for rango, cantidad in self.edades.items():
                datos.write(struct.pack(formato, rango.encode(), str(cantidad).encode()))

    def almacenar_promedio_de_edad_por_provincia(self):
         with open("promedio_de_edad_por_provincia.txt", "wb") as datos:
             formato = "%ds%ds" % (20, 5)
             for provincia, promedio in self.promediar_edad_por_provincia():
                 datos.write(struct.pack(formato, rango.encode(), str(cantidad).encode()))

    def almacenar_ranking_de_infectados_por_provincias(self):
        rank_ordenado = sorted(self.ranking.items(), key=operator.itemgetter(1), reverse=True)
        with open("ranking_de_infectados_por_provincias.txt", "wb") as datos:
            formato = "%ds%ds" % (20, 8)
            for provincia, infectados in self.promediar_edad_por_provincia():
                datos.write(struct.pack(formato, rango.encode(), str(infectados).encode()))

    def main(self):
        with open(self.archivo, encoding="utf-8" ) as archivo:
            entrada = csv.DictReader(archivo)
            for linea in entrada:
                if linea["clasificacion_resumen"] == "Confirmado":
                    self.casos_por_provincia(linea["residencia_provincia_nombre"], linea["sexo"])
                    self.casos_por_edad(linea["edad"], linea["edad_años_meses"])
                    self.agregar_al_promedio(linea["residencia_provincia_nombre"], linea["edad"], linea["edad_años_meses"])
                    self.agregar_al_ranking(linea["residencia_provincia_nombre"])
