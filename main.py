
# from DTOs.DTOCuentaBancaria import DTOCuentaBancaria
from Menu import Menu
from Servicios.ConsignacionesCajero import ConsignacionesCajero
from Servicios.RetirosCajero import RetirosCajero
from Repositorio.CuentasBancarias import CuentasBancarias

# cuentaBancaria = DTOCuentaBancaria(
#     idCuentaBancaria=1,
#     saldo = 0,
#     )

#Instancias de clases 
menu = Menu()
consignaciones = ConsignacionesCajero()
retirosCajeros = RetirosCajero()
cuentaBancaria = CuentasBancarias(1,2323,"Carlos Mora","Contraseña123")

bucleEjecucion:bool = True


while bucleEjecucion:
    opcionSeleccionada = menu.SeleccionarOpcion()
    print("informacion dentro del selec" +str(opcionSeleccionada))
    if(opcionSeleccionada == 1):
        consignaciones.RealizarConsignacion(200,cuentaBancaria);
    else:
        retirosCajeros.realizarRetiro(123,cuentaBancaria);
