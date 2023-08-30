from Utilidades.IO import leerTextoPorTeclado,leerNumerosPositivos
class Usuarios:
    def __init__(self) -> None:
        pass

    def MostrarUsuariosRegistrados(self):
        print("==================================================")
        print("=====Informacion del Usuario======================")
        print("==================================================")
        print("Nombre: ",self.nombreCompleto)
        print("Numero de identificacion: ",self.numeroCedula)
        print("==================================================")

    def GenerarNuevoUsuario(self,identifiadorAnterior = 0):
        self.identifiador = identifiadorAnterior + 1
        self.nombreCompleto = leerTextoPorTeclado()
        self.numeroCedula = leerNumerosPositivos()

    