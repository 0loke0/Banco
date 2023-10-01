import React, { FC } from 'react'
import { IUsuarios } from '../Interfaces/InterfaceUsuarios'
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

interface IContenedorUsuario {
  usuarios: IUsuarios[]
}
const ContenedorUsuarios:FC<IContenedorUsuario> = ({usuarios}) => {
  return <>
    { usuarios != undefined && usuarios.length > 0 &&
        <Contenedor>
          <ListGroup>
          {usuarios.map((user:IUsuarios)=>{
            return (
            <SListGroupItem>           
              Nombre de usuario: {user.nombreCompleto} <br/>
              Numero de cedula: {user.numeroCedula}
            </SListGroupItem>)})}
          </ListGroup>
        </Contenedor>
        }
  </>
}

export default ContenedorUsuarios