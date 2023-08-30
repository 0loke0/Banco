
class CuentasBancarias:   
    
    def __init__(self,idCuentaBancaria,saldo,propietario,contrasena) -> None:
        self.idCuentaBancaria : int = idCuentaBancaria
        self.saldo : int = saldo,
        self.propietario : str = propietario
        self.contrasena : str = contrasena

    def MostrarInformacionUsuario(self):
        print("==================================================")
        print("Usuario",self.propietario,"su saldo actual \nde la cuenta",self.idCuentaBancaria,"es:" )
        print("==================================================")     
        print(self.saldo[0] if type(self.saldo) == tuple else self.saldo )
        print("==================================================")
    
    

    
       
    


