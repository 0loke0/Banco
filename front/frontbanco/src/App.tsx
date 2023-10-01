import React ,{ FC, useEffect, useState }from 'react';
import logo from './logo.svg';
import './App.css';
import UsuarioBanco from './Usuario/UsuarioBanco';
import { ICuentasBancarias, IOperacionBancaria, IUsuarios } from './Interfaces/InterfaceUsuarios';
import ContenedorUsuarios from './Usuario/ContenedorCuentas';
import CuentaBancaria from './CuentaBancaria/CuentaBancaria';
import { Col, Container, Row } from 'react-bootstrap';
import ContenedorCuentasBancaria from './CuentaBancaria/ContenedorCuentasBancaria';
import Operaciones from './Operaciones/Operaciones';

function App() {
  const [usuarios, setusuarios] = useState<IUsuarios[]>([])
  const [cuentasBancarias, setcuentasBancarias] = useState<ICuentasBancarias[]>([])
  
  useEffect(() => {
    
  }, [])
  
  const agregarUsuarios = (nuevoUsuario:IUsuarios) =>  {    
    var temUsuario:IUsuarios[] = [...usuarios];    
    temUsuario.push(nuevoUsuario);    
    setusuarios(temUsuario);
  }
  
  const agregarCuentaBancaria = (cuentaBancaria:ICuentasBancarias) =>  {    
    var temCuentasBancarias:ICuentasBancarias[] = [...cuentasBancarias];    
    temCuentasBancarias.push(cuentaBancaria);    
    setcuentasBancarias(temCuentasBancarias);
  }

  const aplicarModificacionCuentaBancaria =(nuevaOperacion:IOperacionBancaria)=>{
    var tempCuentasBancarias = [...cuentasBancarias]
    var cuentas = tempCuentasBancarias.find(
      f=>f.numeroCedulaPropietario == nuevaOperacion.numeroCedulaPropietario  
      && f.tipoCuentaBancaria == nuevaOperacion.tipoCuentaBancaria)    
      var valorAOperar:number = nuevaOperacion.cantidadOperacion * 1  
      cuentas!.saldo += valorAOperar
    setcuentasBancarias(tempCuentasBancarias);
  }


  return (
    <div className="BackgroundApp" style={{padding:"40px"}}>     
    <Container>
      <Row>
        <Col> 
        <UsuarioBanco agregarUsuarios={agregarUsuarios}/>
        <ContenedorUsuarios usuarios={usuarios}/>
      </Col>
      <Col> 
        {usuarios.length > 0 && <>
            <CuentaBancaria agregarCuentaBancaria={agregarCuentaBancaria} usuarios={usuarios}/>
            <ContenedorCuentasBancaria  cuentasBancarias={cuentasBancarias}/>
          </>
        }
      </Col>
      <Col> 
        {cuentasBancarias.length > 0 && 
            <Operaciones cuentasBancarias={cuentasBancarias} AplicarModificaciones={aplicarModificacionCuentaBancaria}/>          
        }
      </Col>
      </Row>

    </Container>
     
     
    </div>
  );
}

export default App;
