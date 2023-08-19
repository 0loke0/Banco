from Utilidades.IO import leerOpcionNumericaPorTeclado,leerCantidadMovimiento
class Menu:

    def __init__(self) -> None:
        pass
    

    def SeleccionarOpcion(self) -> int:
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
        return leerCantidadMovimiento()



   



