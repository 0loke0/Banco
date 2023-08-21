from Validaciones.numeros import ValidarOpcionNumerica,ValidarNumeroPositivo
    

def leerOpcionNumericaPorTeclado(cantidadOpciones = 0)-> int:
    numero = 0
    try:
        numero = int(input())
    except:
        raise ValueError("La opcion ingresada no es un numero")                
    
    validacionCorrecta = ValidarOpcionNumerica(numero,cantidadOpciones)
    if(validacionCorrecta):
        print("se ha selecionado la opcion", str(numero))
        return numero        
    else: 
        print("la opcion seleccionada no es valida")
        return -1

def leerCantidadMovimiento()-> int:
    numero = 0
    try:
        numero = int(input())
    except:
        raise ValueError("La opcion ingresada no es un numero")                
    
    validacionCorrecta = ValidarNumeroPositivo(numero)
    
    if(validacionCorrecta):
        return numero        
    else: 
        print("La cantidad ingresada no es valida")
        return 0


   
    