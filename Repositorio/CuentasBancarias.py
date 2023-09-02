from Utilidades.IO import LeerTextoPorTeclado,LeerNumerosPositivos
from Utilidades.IO import LeerOpcionNumericaPorTeclado
from Repositorio.Usuarios import Usuarios


class CuentasBancarias(Usuarios):   
    
    def __init__(self,usuarios:[Usuarios]) -> None:
        self.idCuentaBancaria : int = 0,
        self.saldo : int = 0,
        self.tipoCuentaBancaria: int = 0
        self.usuariosCreados: [Usuarios] = usuarios
        self.usuario = None

    def MostrarInformacionCuentaBancaria(self):
        self.usuario.MostrarUsuariosRegistrados();
        print("==================================================")
        print("=========== Cuenta bancaria",self.ConvertirTipoDeCuentaBancaria())
        print("==================================================")
        print("Su saldo actual de la cuenta",self.idCuentaBancaria,"es:" )
        print("==================================================")     
        print(self.saldo[0] if type(self.saldo) == tuple else self.saldo )
        print("==================================================")


    def GenerarNuevaCuentaBancaria(self,identifiadorAnterior = 0)-> bool:
        crearNuevoUsuario = True
        print("==================================================")
        self.idCuentaBancaria = identifiadorAnterior + 1
        print("Numero de identificacion del propietario: ")
        self.numeroCedula = LeerNumerosPositivos()    
        validacionCorrecta = self.ValidarExistenciaDeUsuarioCreado(self.numeroCedula);
        if validacionCorrecta:
            self.tipoCuentaBancaria = self.AsignarTipoDeCuentaBancaria(); 
            print("==================================================")            
        else:
            crearNuevoUsuario = False
        return crearNuevoUsuario


    
       
    def AsignarTipoDeCuentaBancaria(self) -> int:
        print("==================================================")
        print("==========Selecione el tipo de Cuenta ============")
        print("==================================================")
        print("==================================================")
        print("1: Ahorro")
        print("2: Corriente")
        print("3: Nomina")
        print("==================================================")
        print("==================================================")
        return LeerOpcionNumericaPorTeclado(3);

    def ConvertirTipoDeCuentaBancaria(self)-> str:
        indentificadorTipoCuenta = self.tipoCuentaBancaria
        if(indentificadorTipoCuenta == 1):
            return "Ahorro"
        if(indentificadorTipoCuenta == 2):
            return "Corriente"
        if(indentificadorTipoCuenta == 3):
            return "Nomina"
        return ""
    
    def ValidarExistenciaDeUsuarioCreado(self,numeroCedula:int):
        validacionCorrecta = True
        for usuario in self.usuariosCreados:
            if usuario.numeroCedula == numeroCedula:
                self.usuario = usuario
                return validacionCorrecta
            
        validacionCorrecta = False
        print("El usuario con la identifiacion",numeroCedula,"No esta registrado")

        return validacionCorrecta