numeros = [6,78,45,67,34,5,9,52]

def demo1(lista):
    resultado = []
    for i in lista:
        return i * 5
    
def demo2(lista):
    resultado = []
    for i in lista:
        resultado.append(i * 5)

    return resultado

def demo3(lista):
    for i in lista:
        yield (i * 5)

print("Resultado: ",demo3(numeros))
print("Resultado lsta: ",list(demo3(numeros)))

generator = demo3(numeros)
print(next(generator))
print(next(generator))
print(next(generator))

generador = demo3(numeros)
for i in generator:
    print(">>>", i)

generator2 = ((i * 5) for i in numeros)
print("Next >>>>",next(generator2))
print("Next >>>>",next(generator2))
for i in generator2:
    print ("For >", i)