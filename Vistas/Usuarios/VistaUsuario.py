from Utilidades.IO import LeerTextoPorTeclado,LeerNumerosPositivos
from abc import ABC,abstractmethod
from Repositorio.Usuarios import Usuarios

    
class VistaUsuarios():
    def __init__(self,usuarios:Usuarios) -> None:
        self.usuarios = usuarios;
        

    def MostrarUsuariosRegistrados(self):
        print("==================================================")
        print("==================================================")
        print("===== Informacion del Usuario",self.usuarios.identificador,"==================")
        print("==================================================")
        print("Nombre: ",self.usuarios.nombreCompleto)
        print("Numero de identificacion: ",self.usuarios.numeroCedula)
        print("==================================================")
        print("==================================================")

    
