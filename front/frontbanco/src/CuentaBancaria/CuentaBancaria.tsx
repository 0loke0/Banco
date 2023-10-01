import { type } from 'os';
import React, { FC, useState } from 'react'
import { Button, Form, ListGroup, ListGroupItem } from 'react-bootstrap';
import styled from 'styled-components';
import { ICuentasBancarias, IUsuarios } from '../Interfaces/InterfaceUsuarios';


const Contenedor = styled.div`
  width:400px; 
  border:3px solid #3e4057;
  margin:5px;
  padding:10px;
  border-radius:7px;
`;

const SFormSelect = styled(Form.Select)`
  margin:3px 3px 20px 3px;  
`;

const STitulo = styled(Form.Group)`
  font-size:large;
  font-weight:900;
  color:#3e4057;  
`;

interface ICuentaBancaria {
  usuarios: IUsuarios[]
  agregarCuentaBancaria:(nuevoCuentaBancaria:ICuentasBancarias)=>void;
}

const CuentaBancaria:FC<ICuentaBancaria> = ({usuarios,agregarCuentaBancaria}) => {
  const [nuevaCuentaBancaria, setnuevaCuentaBancaria] = useState<ICuentasBancarias>({numeroCedulaPropietario:0,tipoCuentaBancaria:"",saldo:0})
    
  const actualizarNuevoUsuario = (propiedad: string, valor: any) => {   
    setnuevaCuentaBancaria({ ...nuevaCuentaBancaria, [propiedad]: valor });
  } 

  const agregarNuevoUsuario =()=>{
    agregarCuentaBancaria(nuevaCuentaBancaria);
  }

 return(
 <Contenedor>
    <Form >
      <STitulo className="mb-3" controlId="formGroupEmail">Cuentas Bancarias</STitulo>
    <Form.Label> Usuario </Form.Label>
    <SFormSelect onChange={(e)=>actualizarNuevoUsuario("numeroCedulaPropietario",e.target.value)}>
        <option>Seleccione el usuario</option>
        {usuarios.map(user=>
        <option value={user.numeroCedula}>{user.nombreCompleto}</option>
        ) }
    </SFormSelect>
    <Form.Label> Tipo de cuenta </Form.Label>    
    <SFormSelect onChange={(e)=>actualizarNuevoUsuario("tipoCuentaBancaria",e.target.value)}> 
      <option>Selecione tipo de cuenta </option>
      <option value="Ahorro">Ahorro</option>
      <option value="Corriente">Corriente</option>
      <option value="Nomina">Nomina</option>
    </SFormSelect>      
    </Form>
  <Button variant="primary" onClick={agregarNuevoUsuario}>Guardar</Button>          
</Contenedor>)
}

export default CuentaBancaria