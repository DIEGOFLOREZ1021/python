#Calculo de edad y si es mayor de edad.

from datetime import datetime
from time import time

fechaHoy = datetime.now().date()
nac = input("Indica tu fecha de nacimiento: DD-MM-AAAA")
fechaNacimiento = datetime.strptime(nac, "%d-%m-%Y").date()


