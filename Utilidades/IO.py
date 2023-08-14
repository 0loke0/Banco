
from Validaciones.numeros import ValidarOpcionNumerica
    

def leerOpcionNumericaPorTeclado(cantidadOpciones = 0)-> int:
    numero = 0
    try:
        numero = int(input())
    except:
        raise ValueError("La opcion ingresada no es un numero")                
    
    validacionCorrecta = ValidarOpcionNumerica(numero,cantidadOpciones)
    if(validacionCorrecta):
        print("La opcion ingresada no es un numero "+str(numero))
        return numero
    else: 
        return -1


   
    