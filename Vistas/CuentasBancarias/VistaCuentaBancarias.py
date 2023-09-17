from ..Usuarios.VistaUsuario import VistaUsuarios
from Interfaces.Repositorio import ICuentasBancarias

class VistaCuentaBancarias:

    def __init__(self,cuentaBancaria:ICuentasBancarias) -> None:
        self.cuentaBancaria = cuentaBancaria;

    
    def MostrarInformacionCuentaBancaria(self):
        VistaUsuarios(self.cuentaBancaria.usuario).MostrarUsuariosRegistrados();
        print("==================================================")
        print("=========== Cuenta bancaria",self.MostrarTipoDeCuentaBancariaConvertido())
        print("==================================================")
        print("Su saldo actual de la cuenta",self.cuentaBancaria.idCuentaBancaria,"es:" )
        print("==================================================")     
        print(self.cuentaBancaria.saldo[0] if type(self.cuentaBancaria.saldo) == tuple else self.cuentaBancaria.saldo )
        print("==================================================")

    def MostrarTipoDeCuentaBancariaConvertido(self)-> str:
        indentificadorTipoCuenta = self.cuentaBancaria.tipoCuentaBancaria
        if(indentificadorTipoCuenta == 1):
            return "Ahorro"
        if(indentificadorTipoCuenta == 2):
            return "Corriente"
        if(indentificadorTipoCuenta == 3):
            return "Nomina"
        return ""
    
    