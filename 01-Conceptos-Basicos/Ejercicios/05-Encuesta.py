#############################################################################
#Requerimientos Funcionales
#
#      -> Visualizar la media de opinion 
#      -> Visualizar el numero total de encuestas
#      -> El resultado se muestra al escribir FIN
#      -> El valor de opinion es entre 0 y 10
#############################################################################
#   Utilizando listas de Python, 10 encuestados y valor entre 0-10
#############################################################################
respuesta = 0
listaO = []
listaMay = []
listaMen = []
listaMed = []

while True:
    if respuesta != "fin":
        opinion = int(input("Indicanos tu opinion con valor de 0 a 10: "))
        listaO.append(opinion)
        edad = int(input ("Indicanos tu edad: "))
        if edad < 18:
            listaMen.append(edad)
        elif edad > 17 and edad < 56:
            listaMed.append(edad)
        elif edad > 55:
            listaMay.append(edad)
        elif edad <0 or edad >120:
            print("Edad fuera de rango")
        else:
            print("")
    else:
        break
    respuesta=input("Continuar?")

media = 0
print(listaO)
print(listaMen)
print(listaMay)
print(listaMed)

# Calculo media opinion
for i in range (1,len(listaO),1):
    media = media + listaO[i]
media = media/len(listaO)

# Calculo media edad menor


print("La media de opinion ha sido de ",media)
print("Numero total de encuestas hechas: ",len(listaO))

