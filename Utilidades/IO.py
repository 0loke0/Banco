from Validaciones.numeros import ValidarOpcionNumerica,ValidarNumeroPositivo
from Validaciones.textos import ValidarTexto

def LeerOpcionNumericaPorTeclado(cantidadOpciones = 0)-> int:
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

def LeerNumerosPositivos()-> int:
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
    
def LeerTextoPorTeclado()-> str:
    texto = ""
    try:
        texto = str(input())
    except:
        raise ValueError("El texto ingresado no es correcto")
    
    validacionCorrecta = ValidarTexto(texto);
    if(validacionCorrecta):
        return texto        
    else: 
        raise ValueError("El texto ingresado no es correcto")
        




   
    