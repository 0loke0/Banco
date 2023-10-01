import React, { FC } from 'react'
import { ICuentasBancarias, IUsuarios } from '../Interfaces/InterfaceUsuarios'
import styled from 'styled-components';
import { ListGroup, ListGroupItem } from 'react-bootstrap';


const Contenedor = styled.div`
  width:400px; 
  border:3px solid #3e4057;
  margin:5px;
  padding:10px;
  border-radius:7px;
`;
const SListGroupItem = styled(ListGroupItem)`
  background-color:#8793a3;
  opacity: 0.7;
  color:#26294d;  
  font-weight:600;
`;

interface IContenedorCuentaBancaria{
  cuentasBancarias: ICuentasBancarias[]
}

const ContenedorCuentaBancaria:FC<IContenedorCuentaBancaria> = ({cuentasBancarias}) => {
  return <>
    { cuentasBancarias != undefined && cuentasBancarias.length > 0 &&
        <Contenedor>
          <ListGroup>
          { cuentasBancarias.map((user:ICuentasBancarias)=>{
            return (
            <SListGroupItem>           
              Cedula Propietario: {user.numeroCedulaPropietario} <br/>
              Tipo de cuenta: {user.tipoCuentaBancaria} <br/>
              Saldo: {user.saldo} 
            </SListGroupItem>)})}
          </ListGroup>
        </Contenedor>
        }
  </>
}

export default ContenedorCuentaBancaria