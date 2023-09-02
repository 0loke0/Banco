from Utilidades.IO import LeerTextoPorTeclado,LeerNumerosPositivos

class Usuarios:

    def __init__(self) -> None:
        self.identificador = 0;
        self.nombreCompleto = "";
        self.numeroCedula = 0

    def MostrarUsuariosRegistrados(self):
        print("==================================================")
        print("==================================================")
        print("===== Informacion del Usuario",self.identificador,"==================")
        print("==================================================")
        print("Nombre: ",self.nombreCompleto)
        print("Numero de identificacion: ",self.numeroCedula)
        print("==================================================")
        print("==================================================")

    def GenerarNuevoUsuario(self,identifiadorAnterior = 0):
        print("==================================================")
        self.identificador = identifiadorAnterior + 1
        print("Nombre: ")
        self.nombreCompleto = LeerTextoPorTeclado()
        print("Numero de identificacion: ")
        self.numeroCedula = LeerNumerosPositivos()
        print("==================================================")

    