from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

client = MongoClient("localhost", 27017 )

# Listar los nombres de la base de datos en el motor mongoDB
print(client.list_database_names())

# Sintaxis propia de un objeto
db = client.Northwind

# Sintaxis de coleccion
db2 = client["Northwind"]

# Listar los nombres de las conexiones de la base de datos
print(db.list_collection_names())
print(db2.list_collection_names())

# Seleccionar una conexion de la base de datos
collection = client.Northwind.Customers
collection = client["Northwind"]["Customers"]
collection = db.Customers
collection = db["Customers"]

# Mostrar eñ numero de documentos (registros) en la conexion
print(collection.estimated_document_count()," Documentos en ",collection.name)

# LEER DATOS
result = collection.find_one({"Country":"USA"})
pprint(result)
