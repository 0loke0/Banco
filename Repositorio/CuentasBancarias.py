from Utilidades.IO import LeerNumerosPositivos
from Vistas.CuentasBancarias.VistaMenuCuentaBancaria import VistaMenuCuentaBancaria
from Repositorio.Usuarios import Usuarios
from Interfaces.Repositorio import ICuentasBancarias

class CuentasBancarias(ICuentasBancarias,Usuarios):   
    
    def __init__(self,usuarios:[Usuarios]) -> None:
        self.idCuentaBancaria : int = 0,
        self.saldo : int = 0,
        self.tipoCuentaBancaria: int = 0
        self.usuariosCreados: [Usuarios] = usuarios
        self.usuario = None

   

    def GenerarNuevaCuentaBancaria(self,identifiadorAnterior = 0)-> bool:
        crearNuevoUsuario = True
        print("==================================================")
        self.idCuentaBancaria = identifiadorAnterior + 1
        print("Numero de identificacion del propietario: ")
        self.numeroCedula = LeerNumerosPositivos()    
        validacionCorrecta = self.ValidarExistenciaDeUsuarioCreado(self.numeroCedula);
        if validacionCorrecta:
            self.tipoCuentaBancaria = VistaMenuCuentaBancaria().AsignarTipoDeCuentaBancaria(); 
            print("==================================================")            
        else:
            crearNuevoUsuario = False
        return crearNuevoUsuario

        
    def ValidarExistenciaDeUsuarioCreado(self,numeroCedula:int):
        validacionCorrecta = True
        for usuario in self.usuariosCreados:
            if usuario.numeroCedula == numeroCedula:
                self.usuario = usuario
                return validacionCorrecta
            
        validacionCorrecta = False
        print("El usuario con la identifiacion",numeroCedula,"No esta registrado")

        return validacionCorrecta