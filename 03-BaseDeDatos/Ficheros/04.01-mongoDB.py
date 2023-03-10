from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

# Crear el objeto que representa el cliente para trabajar con la base de datos
# Se requiere a cadena de conexion
client = MongoClient("localhost", 27017 )

# Mostrar el estado del servidor
# Nos posicionamos en una base de datos utilizando el objeto cliente
db = client.admin

# Ejecutamos un comando sobre la base de datos
# Los comando nos permiten INSERTAR, ACTUALIZAR, ELIMINAR Y LEER informacion de la base de datos

# El comando servarStatus nos retorna el estado del servidor en JSON
status = db.command("serverStatus")
pprint(status)