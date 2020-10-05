import Cliente
import Cuenta
import CuentaMultipersona
import CuentaSueldo
import CuentaSueldoPlus
import pickle
import shelve
import json

def almacenar_en_json(clientes):
    datos = {}
    datos["clientes"] = []
    for cliente in clientes:
        datos["clientes"].append({
            "nombre": cliente._nombre,
            "dni": cliente._dni
        })
    with open("almacenamiento.json", "w") as archivo_json:
        json.dump(datos, archivo_json)

def almacenar_en_pickle(objetos):
    with open("almacenamiento.pickle", "wb") as archivo_pickle:
        for objeto in objetos:
            pickle.dump(objetos, archivo_pickle)

def almacenar_en_shelve(llave, objeto):
    with shelve.open("almacenamiento.db") as archivo_shelve:
        archivo_shelve[llave] = objeto

def recuperar_datos_en_json():
    with open("almacenamiento.json") as archivo_json:
        datos = json.load(archivo_json)
        for cliente in datos["clientes"]:
            print("nombre: ", cliente["nombre"])
            print("dni: ", cliente["dni"])

def recuperar_datos_en_pickle():
    with open("almacenamiento.pickle", "rb") as objetos:
        while True:
            try:
                lista = pickle.load(objetos)
            except EOFError:
                break
    for objeto in lista:
        print(objeto)

def recuperar_datos_en_shelve():
    with shelve.open("almacenamiento.db") as objetos:
        for (clave, valor) in objetos.items():
            print(clave, ": ", valor)
