from Utilidades.IO import LeerOpcionNumericaPorTeclado
from Interfaces.Repositorio import ICuentasBancarias
from Vistas.CuentasBancarias.VistaCuentaBancarias import VistaCuentaBancarias
class VistaMenuCuentaBancaria:
    
      def __init__(self) -> None:
          pass

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

      def SeleccionarCuentaBancaria(self,cuentasBancarias:[ICuentasBancarias])->ICuentasBancarias:
        print("==================================================")
        print("======Selecione la cuenta Bancaria=====")
        print("==================================================")
        for cuentaBancaria in cuentasBancarias:
            print( cuentaBancaria.idCuentaBancaria," - ",cuentaBancaria.usuario.nombreCompleto," - ",cuentaBancaria.usuario.numeroCedula ," - ", VistaCuentaBancarias(cuentaBancaria).MostrarTipoDeCuentaBancariaConvertido())
            
        print("==================================================")
        print("==================================================")
        opcionSelecionada = LeerOpcionNumericaPorTeclado(len(cuentasBancarias)+1)        
        return cuentasBancarias[opcionSelecionada-1]

