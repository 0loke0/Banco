export interface IUsuarios {
    identificador:number;    
    nombreCompleto:string;
    numeroCedula:number;
  }

  export interface ICuentasBancarias {
    numeroCedulaPropietario: number;
    tipoCuentaBancaria:string;
    saldo:number;   
  }

  export interface IOperacionBancaria {
    numeroCedulaPropietario:number;   
    tipoCuentaBancaria:string;
    tipoDeOperacion:string;
    cantidadOperacion:number;
  }