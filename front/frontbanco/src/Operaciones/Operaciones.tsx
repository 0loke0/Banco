import React, { FC, useState } from 'react'
import { ICuentasBancarias, IOperacionBancaria } from '../Interfaces/InterfaceUsuarios'
import styled from 'styled-components';
import { Button, Form } from 'react-bootstrap';

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

const SInput = styled.div`
  margin:3px 3px 20px 3px;  
`;

interface IOperaciones{
    cuentasBancarias: ICuentasBancarias[]
    AplicarModificaciones:(nuevaOperacion:IOperacionBancaria)=>void;
}

const Operaciones:FC<IOperaciones> = ({cuentasBancarias,AplicarModificaciones}) => {

    const [nuevaOperacion, setnuevaOperacion] = useState<IOperacionBancaria>({cantidadOperacion:0,tipoCuentaBancaria:"",numeroCedulaPropietario:0,tipoDeOperacion:""})

    const actualizarNuevoUsuario = (propiedad: string, valor: any) => {        
        setnuevaOperacion({ ...nuevaOperacion, [propiedad]: valor });    } 

    const implementarModificaciones =()=> {
        if (nuevaOperacion.tipoDeOperacion == "Retiro" ) {
            nuevaOperacion.cantidadOperacion = nuevaOperacion.cantidadOperacion * -1
            setnuevaOperacion(nuevaOperacion)
        }
        AplicarModificaciones(nuevaOperacion);
    }

    return (
        <Contenedor>
            <Form >
            <STitulo className="mb-3" controlId="formGroupEmail">Operaciones</STitulo>
            <SFormSelect onChange={(e)=>actualizarNuevoUsuario("numeroCedulaPropietario",e.target.value)}>
            <option>Seleccione el usuario</option>
            {cuentasBancarias.map(cuenta=>
            <option value={cuenta.numeroCedulaPropietario}>{cuenta.numeroCedulaPropietario}</option>
            ) }
            </SFormSelect>
            {nuevaOperacion.numeroCedulaPropietario != 0 &&      
                
                <SFormSelect onChange={(e)=>actualizarNuevoUsuario("tipoCuentaBancaria",e.target.value)}>
                <option>Seleccione el tipo de cuenta</option>
                {cuentasBancarias.filter(f=>f.numeroCedulaPropietario == nuevaOperacion.numeroCedulaPropietario).map(cuenta=>
                <option value={cuenta.tipoCuentaBancaria}>{cuenta.tipoCuentaBancaria}</option>
                ) }          
            </SFormSelect>
            }
            <Form.Label> Usuario </Form.Label>
            <SFormSelect onChange={(e)=>actualizarNuevoUsuario("tipoDeOperacion",e.target.value)}>
                <option>Seleccione el usuario</option>  
                <option value="Retiro">Retiro</option>
                <option value="Consignacion">Consignacion</option>       
            </SFormSelect>
            <SInput> 
            <Form.Label> Cantidad </Form.Label>
            <Form.Control type="text" placeholder="$" onChange={(e)=>actualizarNuevoUsuario("cantidadOperacion",e.target.value)}/>
            </SInput>        
            </Form>
        <Button variant="primary" onClick={implementarModificaciones}>Aplicar</Button>          
        </Contenedor>
    )
}

export default Operaciones