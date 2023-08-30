
from Menu import Menu
from Servicios.ConsignacionesCajero import ConsignacionesCajero
from Servicios.RetirosCajero import RetirosCajero
from Repositorio.CuentasBancarias import CuentasBancarias
from Repositorio.Usuarios import Usuarios
from Utilidades.Pantalla import BorraPantalla
from time import sleep

#Instancias de clases 
menu = Menu()
consignaciones = ConsignacionesCajero()
retirosCajeros = RetirosCajero()
cuentaBancaria = CuentasBancarias(958547333,2323,"Carlos Mora","Contraseña123")
usuarios = Usuarios();



def GenerarUsuarios():
    bucleEjecucion:bool = True
    while bucleEjecucion:
        opcionSeleccionada = menu.SelecionarOpcionesCrearNuevoUsuario()
        BorraPantalla()
        if(opcionSeleccionada == 1):
            usuarios.GenerarNuevoUsuario()
        if(opcionSeleccionada == 2):
            bucleEjecucion = False;
            break


def RealizarAccionesCajero():
    bucleEjecucion:bool = True
    while bucleEjecucion:
        opcionSeleccionada = menu.SeleccionarOpcionesCajero()     
        BorraPantalla()
        if(opcionSeleccionada == 1):
            consignaciones.RealizarConsignacion(menu.SeleccionarCantidadIngresada(),cuentaBancaria);
        if(opcionSeleccionada == 2):
            retirosCajeros.RealizarRetiro(menu.SeleccionarCantidadIngresada(),cuentaBancaria);
        if(opcionSeleccionada == 3):     
            cuentaBancaria.MostrarInformacionUsuario()   
            bucleEjecucion = False;
            break
        sleep(5)
        BorraPantalla()



GenerarUsuarios()
RealizarAccionesCajero()