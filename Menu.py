from Utilidades.IO import leerOpcionNumericaPorTeclado,leerNumerosPositivos
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
        return leerOpcionNumericaPorTeclado(2)
    
    def SeleccionarOpcionesCajero(self) -> int:
        print("==================================================")
        print("======Seleccione la opción que desea realizar=====")
        print("==================================================")
        print("1: Consignar")
        print("2: Retirar")
        print("3: Terminar Operacion")
        print("==================================================")
        print("==================================================")
        return leerOpcionNumericaPorTeclado(3)
    

    def SeleccionarCantidadIngresada(self) -> int:
        print("==================================================")
        print("==============Digite la cantidad:=================")
        print("==================================================")
        return leerNumerosPositivos()



   



