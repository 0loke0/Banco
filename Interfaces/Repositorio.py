from abc import ABC,abstractmethod

class ICreadoresElementosConConsecutivos(ABC):
    @abstractmethod
    def GenerarNuevo(self,identifiadorAnterior = 0):
        """"""   

class IUsuarios(ICreadoresElementosConConsecutivos,ABC):    
    pass

class ICuentasBancarias(ICreadoresElementosConConsecutivos,ABC):   
    @abstractmethod
    def ValidarExistenciaDeUsuarioCreado(self,numeroCedula:int):
        """"""

