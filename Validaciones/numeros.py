    
def ValidarOpcionNumerica(numero:int, cantidadOpciones:int )-> bool:
    validacionCorreta: bool = True
    mensajesError: str = ""
                 
    if (numero <= 0):
        mensajesError += "El numero ingresado es menor a 0: " + str(numero)
    if ( (cantidadOpciones != 0) & (numero > cantidadOpciones )):
        mensajesError += "El numero ingresado no se encuentra dentro de las opciones permitidas: " + str(numero)
    
    print("mensajesError"+mensajesError)
    if (mensajesError != ""):
        print(mensajesError)
        validacionCorreta = False
        
    return validacionCorreta;
    