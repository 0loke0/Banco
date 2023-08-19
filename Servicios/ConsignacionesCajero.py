from datetime import date
from DTOs.DTOCuentaBancaria import DTOCuentaBancaria

class ConsignacionesCajero:
    
    def __init__(self) -> None:
        pass
        
        
    def RealizarConsignacion(self,cantidad:int,cuentaBancaria):
        if(type(cuentaBancaria.saldo) == tuple): 
            cuentaBancaria.saldo = (int(cuentaBancaria.saldo[0]) + cantidad)
        else:
            cuentaBancaria.saldo += cantidad   
        print("Se realiza una consignacion: Saldo actual ", cuentaBancaria.saldo)