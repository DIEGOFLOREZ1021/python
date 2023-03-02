from datetime import datetime
from time import time

dt1 = datetime.now()
print("Fecha 1: " , dt1 )
print("Hora: ", dt1.hour)
print("Minuto: ", dt1.minute)
print("Segundo: ", dt1.second)

dt2 = datetime.now().date()
print("Fecha 2: " , dt2 )
print("Dia: ", dt2.day)
print("Mes: ", dt2.month)
print("Año: ", dt2.year)


strFecha = "21-10-2003"
dt3= datetime.strptime(strFecha, "%d-%m-%Y").date()

print("Fecha de nacimiento", dt3)
print("Fecha de nacimiento", dt3.strftime("%d of %B, %Y"))

print("Edad: ",dt2-dt3, "Años")

