from abc import ABC,abstractmethod

class ICuentasBancarias(ABC):    
    @abstractmethod
    def GenerarNuevaCuentaBancaria(self,identifiadorAnterior = 0)-> bool:
        """"""
    @abstractmethod
    def ValidarExistenciaDeUsuarioCreado(self,numeroCedula:int):
        """"""

class IUsuarios(ABC):    
    @abstractmethod
    def GenerarNuevoUsuario(self,identifiadorAnterior = 0):
        """"""   