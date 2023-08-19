    
def ValidarOpcionNumerica(numero:int, cantidadOpciones:int )-> bool:
    validacionCorreta: bool = True
    mensajesError: str = ""
                 
    if (ValidarNumeroPositivo(numero) == False):
        mensajesError += "El numero ingresado es menor a 0: " + str(numero)
    if ( (cantidadOpciones != 0) & (numero > cantidadOpciones )):
        mensajesError += "El numero ingresado no se encuentra dentro de las opciones permitidas: " + str(numero)       
    if (mensajesError != ""):
        print("mensajesError"+mensajesError)       
        validacionCorreta = False
        
    return validacionCorreta;

def ValidarResultadoRestaInferiorACero(valorInicial:int,valorResta:int)->bool:
    if (valorInicial < valorResta):
        return True;
    return False


def ValidarNumeroPositivo(numero:int)-> bool:
    if (numero > 0):
        return True
    return False
