
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



usuariosRegistrados = []
cuentasBancariasRegistradas = []

def GenerarUsuarios():
    bucleEjecucion:bool = True
    while bucleEjecucion:
        opcionSeleccionada = menu.SelecionarOpcionesCrearNuevoUsuario()
        BorraPantalla()
        if(opcionSeleccionada == 1):
            usuarios = Usuarios();
            print("Usuarios creados",len(usuariosRegistrados))
            usuarios.GenerarNuevoUsuario() if len(usuariosRegistrados) == 0 else usuarios.GenerarNuevoUsuario(len(usuariosRegistrados))
            usuariosRegistrados.append(usuarios)  
            BorraPantalla()
        if(opcionSeleccionada == 2):
            for usuario in usuariosRegistrados:
                usuario.MostrarUsuariosRegistrados()
            bucleEjecucion = False;
            sleep(5)  
        BorraPantalla()

def CrearCuentaBancaria():
    bucleEjecucion:bool = True
    while bucleEjecucion:
        opcionSeleccionada = menu.SelecionarOpcionesCrearNuevaCuentaBancaria()     
        BorraPantalla()
        if(opcionSeleccionada == 1):
            cuentaBancaria = CuentasBancarias(usuariosRegistrados)
            crearNuevaCuenta = True;
            print("Cuentas bancarias creadas",len(cuentasBancariasRegistradas))
            if len(cuentasBancariasRegistradas) == 0:
                crearNuevaCuenta = cuentaBancaria.GenerarNuevaCuentaBancaria()  
            else:
                crearNuevaCuenta = cuentaBancaria.GenerarNuevaCuentaBancaria(len(cuentasBancariasRegistradas))
            if crearNuevaCuenta:
                cuentasBancariasRegistradas.append(cuentaBancaria)
        if(opcionSeleccionada == 2):
            for cuenta in cuentasBancariasRegistradas:
                cuenta.MostrarInformacionCuentaBancaria()
            bucleEjecucion = False;
            sleep(5)      
        BorraPantalla()

def RealizarAccionesCajero():
    bucleEjecucion:bool = True
    while bucleEjecucion:
        cuentaBancaria = menu.SeleccionarCuentaBancaria(cuentasBancariasRegistradas)
        opcionSeleccionada = menu.SeleccionarOpcionesCajero()       
        BorraPantalla()
        if(opcionSeleccionada == 1):
            consignaciones.RealizarConsignacion(menu.SeleccionarCantidadIngresada(),cuentaBancaria);
        if(opcionSeleccionada == 2):
            retirosCajeros.RealizarRetiro(menu.SeleccionarCantidadIngresada(),cuentaBancaria);
        if(opcionSeleccionada == 3):     
            cuentaBancaria.MostrarInformacionCuentaBancaria()   
            bucleEjecucion = False;
            break
        sleep(5)
        BorraPantalla()


    
    

GenerarUsuarios()
CrearCuentaBancaria()
RealizarAccionesCajero()