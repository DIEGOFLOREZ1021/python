
numeros = [34 , 3 , 56 , 90 , 346 , 876 , 12 , 129]

def numMayores(lista):
    resultado = []

    for i in numeros:
        if (i > 100):
            resultado.append(i)

    return resultado 

def Filtrado(formula,datos):
    resultado = []
    for i in datos:
        if (formula(i)==True):
            resultado.append(i)

    return resultado

print(">>> ", Filtrado(lambda x: x > 100, numeros))

print ("Valores mayores de 100",list(filter(lambda x: x > 100,numeros)))
