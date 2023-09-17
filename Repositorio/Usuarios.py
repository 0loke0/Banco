from Utilidades.IO import LeerTextoPorTeclado,LeerNumerosPositivos
from Interfaces.Repositorio import IUsuarios

class Usuarios(IUsuarios):

    def __init__(self) -> None:
        self.identificador = 0;
        self.nombreCompleto = "";
        self.numeroCedula = 0

    def GenerarNuevoUsuario(self,identifiadorAnterior = 0):
        print("==================================================")
        self.identificador = identifiadorAnterior + 1
        print("Nombre: ")
        self.nombreCompleto = LeerTextoPorTeclado()
        print("Numero de identificacion: ")
        self.numeroCedula = LeerNumerosPositivos()
        print("==================================================")
    