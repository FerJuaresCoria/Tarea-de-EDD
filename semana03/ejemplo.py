from Cliente import Cliente
from Cuenta import Cuenta
from CuentaMultipersona import CuentaMultipersona
from CuentaSueldo import CuentaSueldo
from CuentaSueldoPlus import CuentaSueldoPlus
import Persistencia

if __name__ == '__main__':
    cliente = Cliente()
    cuenta = Cuenta()
    cuenta_multipersona = CuentaMultipersona()
    cuenta_sueldo = CuentaSueldo()
    cuenta_sueldo_plus = CuentaSueldoPlus()
    #JSON
    Persistencia.almacenar_en_json([cliente])
    Persistencia.recuperar_datos_en_json()
    #PICKLE
    Persistencia.almacenar_en_pickle([cliente, cuenta, cuenta_multipersona])
    Persistencia.recuperar_datos_en_pickle()
    #SHELVE
    Persistencia.almacenar_en_shelve(cuenta_sueldo._titular, cuenta_sueldo)
    Persistencia.recuperar_datos_en_shelve()
