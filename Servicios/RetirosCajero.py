
from datetime import date

class RetirosCajero:
    
    def __init__(self) -> None:
        pass
    
    def realizarRetiro(self,cantidad:int,cuentaBancaria):
        if(type(cuentaBancaria.saldo) == tuple): 
            cuentaBancaria.saldo = (int(cuentaBancaria.saldo[0]) - cantidad)
        else:
            cuentaBancaria.saldo -= cantidad   
        print("Se realiza un retiro: Saldo actual ", cuentaBancaria.saldo)
