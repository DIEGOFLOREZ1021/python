######################################################
#IF - ELIF - ELSE
"""
a = 10
b = 20

if ( a > b ):
    print("El numero ",a," es mayor.")
    print("Fin")
elif ( b > a ):
    print("El numero ",b," es mayor.")
    print("Fin")
else:
    print("Los dos numeros son iguales")
    print("Fin")
"""
#################################################
# FOR

"""for i in  range (0, 100, 1):                  #Empieza en 0, cuenta 100 veces, va de 1 en 1
    print("Numero ",i)

citricos = ("naranja", "limon", "lima", "pomelo", "mandarina")
print(citricos)
print(citricos[3])                            #una posicion especifica en la cadena
print("Numero de valores: ",len(citricos))    #numero de elementos en la cadena

for i in range (0 , len(citricos) , 1):
    print(i + 1,": " ,citricos[i])  """

########################################################
# WHILE
"""
valor = 0

while (valor < 5):
    valor = valor + 1
    print("El valor es: ",valor)

print("Fin del while")

citricos = ("naranja", "limon", "lima", "pomelo", "mandarina")
x = 0
while (x <len(citricos)):
    print(x + 1,": ",citricos[x])
    x =x+ 1

print("Fin del while")
"""
#################################################################
# TRY - EXCEPT
num1 = 0
num2 = 100

try:
    num3 = num2 / num1
    print("Resultado: ",num3)
except:
    print("No es posible hacer esta operacion...") #permite que el codigo no se pare cuando existe una escepcion
else:
    print("Bloque ELSE")                           #Se ejecuta cuando no hay escepcion
finally:
    print("Operacion terminada con exito")         #Siempre se ejecuta
