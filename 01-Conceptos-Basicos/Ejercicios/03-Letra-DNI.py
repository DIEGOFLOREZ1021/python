##############################################
#Requerimientos Funcionales
#
#
#      -> Calcular la letra del DNI
#      -> Formular: dni % 23
#
#############################################

lista= ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E","T"]

try:
   dni = int(input("Ingresa tu numero de dni sin letra: "))
   formula = dni%23
   print(formula)
   print("Tu DNI es: ",lista[4],dni)
except:
   print("El numero ingresado no es el correcto")

