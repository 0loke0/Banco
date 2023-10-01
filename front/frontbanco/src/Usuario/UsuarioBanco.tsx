import { type } from 'os';
import React, { FC, useEffect, useState } from 'react'
import { Button, Form, ListGroup, ListGroupItem } from 'react-bootstrap';
import styled from 'styled-components';
import { IUsuarios } from '../Interfaces/InterfaceUsuarios';


const Contenedor = styled.div`
  width:400px; 
  border:3px solid #3e4057;
  margin:5px;
  padding:10px;
  border-radius:7px;
`;

const SInput = styled.div`
  margin:3px 3px 20px 3px;  
`;

const STitulo = styled(Form.Group)`
  font-size:large;
  font-weight:900;
  color:#3e4057;  
`;


interface IUsuarioBanco {
   agregarUsuarios:(nuevoUsuario:IUsuarios)=>void;
}

const UsuarioBanco:FC<IUsuarioBanco> = ({agregarUsuarios}) => {    
  const [nuevoUsuario, setnuevoUsuario] = useState<IUsuarios>({identificador:0,nombreCompleto:"",numeroCedula:0})
    
  const actualizarNuevoUsuario = (propiedad: string, valor: any) => {   
    setnuevoUsuario({ ...nuevoUsuario, [propiedad]: valor });
  } 
  
  const agregarNuevoUsuario =()=>{
    agregarUsuarios(nuevoUsuario);
  }
  return (    
    <Contenedor>
      <Form >
        <STitulo className="mb-3" controlId="formGroupEmail">Usuarios</STitulo>
      <SInput> 
          <Form.Label>Nombre</Form.Label>
          <Form.Control type="text" placeholder="Nombre Usuario" onChange={(e)=>actualizarNuevoUsuario("nombreCompleto",e.target.value)}/>
      </SInput>
      <SInput> 
          <Form.Label> Numero de identificacion </Form.Label>
          <Form.Control type="text" placeholder="Numero Identificacion" onChange={(e)=>actualizarNuevoUsuario("numeroCedula",e.target.value)}/>
      </SInput>      
      </Form>
        <Button variant="primary" onClick={agregarNuevoUsuario}>Guardar</Button>          
    </Contenedor>
   )
}

export default UsuarioBanco