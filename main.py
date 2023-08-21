
from Menu import Menu
from Servicios.ConsignacionesCajero import ConsignacionesCajero
from Servicios.RetirosCajero import RetirosCajero
from Repositorio.CuentasBancarias import CuentasBancarias
from Utilidades.Pantalla import BorraPantalla
from time import sleep
#Instancias de clases 
menu = Menu()
consignaciones = ConsignacionesCajero()
retirosCajeros = RetirosCajero()
cuentaBancaria = CuentasBancarias(958547333,2323,"Carlos Mora","Contraseña123")

bucleEjecucion:bool = True



while bucleEjecucion:
    opcionSeleccionada = menu.SeleccionarOpcion()     
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

