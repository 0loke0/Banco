
from DTOs.DTOCuentaBancaria import DTOCuentaBancaria
from Menu import Menu
from Servicios.ConsignacionesCajero import *
from Servicios.ConsignacionesCajero import *

cuentaBancaria = DTOCuentaBancaria(
    idCuentaBancaria=1,
    saldo = 0,
    idPropietario = 1
    )

bucleEjecucion:bool = True
menu = Menu
while bucleEjecucion:
    opcionSeleccionada = menu.seleccionarOpcion()
    if(opcionSeleccionada == 1):
        ConsignacionesCajero(1,0,"Consignacion");
    else:
        print ("Opcion 2")



