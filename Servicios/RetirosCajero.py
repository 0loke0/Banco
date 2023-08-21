from Validaciones.numeros import ValidarResultadoRestaInferiorACero

class RetirosCajero:
    
    def __init__(self) -> None:
        pass
    
    def RealizarRetiro(self,cantidad:int,cuentaBancaria):
        if(type(cuentaBancaria.saldo) == tuple): 
            sinSaldoSuficiente = self.ValidarSaldo(int(cuentaBancaria.saldo[0]),cantidad)
            if(sinSaldoSuficiente): return None
            cuentaBancaria.saldo = (int(cuentaBancaria.saldo[0]) - cantidad)
        else:
            sinSaldoSuficiente = self.ValidarSaldo(cuentaBancaria.saldo,cantidad)     
            if(sinSaldoSuficiente): return None  
            cuentaBancaria.saldo -= cantidad   
        print("Se realiza un retiro: Saldo actual ", cuentaBancaria.saldo)


    def ValidarSaldo (self,saldo:int,cantidadARetirar:int)->bool:
        saldoNoDisponible = ValidarResultadoRestaInferiorACero(saldo,cantidadARetirar)
        if(saldoNoDisponible):
            print("No dispone del saldo suficiente para realizar el retiro")
            print("Saldo actual ", saldo)
        return saldoNoDisponible;
