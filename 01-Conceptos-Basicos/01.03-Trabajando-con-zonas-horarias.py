from datetime import datetime, timedelta, timezone
from pytz import timezone
import pytz

#Mostrar zonas horarias disponibles
#print(pytz.all_timezones)
#print(type(pytz.all_timezones))

#Mostrar la fecha actual
dt = datetime.now()
print(dt)

print(datetime.now(pytz.timezone('US/Eastern')))