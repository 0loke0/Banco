from Utilidades.IO import LeerOpcionNumericaPorTeclado,LeerNumerosPositivos
from Repositorio.CuentasBancarias import CuentasBancarias
class Menu:

    def __init__(self) -> None:
        pass
    
    
    def SelecionarOpcionesCrearNuevoUsuario(self) -> int:
        print("==================================================")
        print("======Creacion de Usuarios=====")
        print("==================================================")
        print("1: Crear nuevo usuario")
        print("2: Terminar Operacion")
        print("==================================================")
        print("==================================================")
        return LeerOpcionNumericaPorTeclado(2)
    
    def SelecionarOpcionesCrearNuevaCuentaBancaria(self) -> int:
        print("==================================================")
        print("======Creacion de Cuenta Bancaria=====")
        print("==================================================")
        print("1: Crear nueva cuenta bancaria")
        print("2: Terminar Operacion")
        print("==================================================")
        print("==================================================")
        return LeerOpcionNumericaPorTeclado(2)
    
    def SeleccionarOpcionesCajero(self) -> int:
        print("==================================================")
        print("======Seleccione la opción que desea realizar=====")
        print("==================================================")
        print("1: Consignar")
        print("2: Retirar")
        print("3: Terminar Operacion")
        print("==================================================")
        print("==================================================")
        return LeerOpcionNumericaPorTeclado(3)
    

    def SeleccionarCantidadIngresada(self) -> int:
        print("==================================================")
        print("==============Digite la cantidad:=================")
        print("==================================================")
        return LeerNumerosPositivos()


    def SeleccionarCuentaBancaria(self,cuentasBancarias:[CuentasBancarias])->CuentasBancarias:
        print("==================================================")
        print("======Selecione la cuenta Bancaria=====")
        print("==================================================")
        for cuentaBancaria in cuentasBancarias:
            print( cuentaBancaria.idCuentaBancaria," - ",cuentaBancaria.usuario.nombreCompleto," - ",cuentaBancaria.usuario.numeroCedula ," - ", cuentaBancaria.ConvertirTipoDeCuentaBancaria())
            
        print("==================================================")
        print("==================================================")
        opcionSelecionada = LeerOpcionNumericaPorTeclado(len(cuentasBancarias)+1)        
        return cuentasBancarias[opcionSelecionada-1]

