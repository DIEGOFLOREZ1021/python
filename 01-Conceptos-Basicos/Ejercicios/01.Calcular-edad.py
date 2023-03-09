#Calculo de edad y si es mayor de edad.

from datetime import datetime
from time import time

fechaHoy = datetime.now().date()
nac = input("Indica tu fecha de nacimiento: DD-MM-AAAA  ")
fechaNacimiento = datetime.strptime(nac, "%d-%m-%Y").date()
print(fechaHoy)

if fechaHoy.month > fechaNacimiento.month:
    edad = fechaHoy.year-fechaNacimiento.year
    print("Edad: ",edad)
else:
    edad = fechaHoy.year-fechaNacimiento.year
    edad = edad - 1
    print("Edad: ",edad)

if edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")

print("Operacion terminada con exito")