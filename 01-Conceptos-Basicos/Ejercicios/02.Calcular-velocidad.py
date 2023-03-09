#Calculo de velocidad y si es alta, moderada o baja

res = "si"

while (res == "si"):

    velocidad = input("Indicanos tu velocidad: ")
    vol = float(velocidad)
    velocidad = vol * 3.6
    print(velocidad)

    if velocidad >= 75:
        print("La velocidad es alta.")
    elif velocidad <75 and velocidad >=35:
        print("La velocidad es moderada")
    elif velocidad < 35:
        print("La velocidad es baja.")
    elif velocidad < 0:
        print("La velocidad integrada es incorrecta")
    else:
        print("Operacion terminada")
    res=input("Deseas continuar?")

print("Operacion Terminada")