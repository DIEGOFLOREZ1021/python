from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

client = MongoClient("localhost", 27017 )
db = client.Northwind
collection = db.Customers

"""
===================================================
 Listado de operadores relacionales
===================================================
$eq - equal - igual
$lt - low than - menor que
$lte - low than equal - menor o igual que
$gt - greater than - mayor que
$gte - greater than equal - mayor o igual que
$ne - not equal - distinto
$in - in - dentro de
$nin - not in - no dentro de
"""

# Ambas consultas buscan clientes de USA (las dos son iguales)
cursor = collection.find({"Country":"USA"})
cursor = collection.find({"Country":{"$eq" : "USA"}}) # Mas especifico

# Todos los clientes que no son de Usa
cursor = collection.find({"Country":{"$ne" : "USA"}})


#print("Numero de documentos en el cursor: ", cursor.count())
print("Numero de documentos sin filtrar: ", collection.estimated_document_count())
print("Numero de documentos filtrado: ", collection.count_documents({"Country":"USA"}))

print("Datos pendientes de leer: ", cursor.alive)

while (cursor.alive):
    pprint(cursor.next())
    print("_______________________________________")

print("Datos pendientes de leer: ", cursor.alive)