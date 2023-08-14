from datetime import date

class ConsignacionesCajero:
    
    def __init__(self,idCuentaBancaria,cantidadDepositada,origen) -> None:
        self.idCuentaBancaria = idCuentaBancaria
        self.cantidadDepositada = cantidadDepositada
        self.origen = origen
        self.fecha = date.today
        
    def realizarConsignacion(cantidad:int):
        print("Se realiza una consignacion")