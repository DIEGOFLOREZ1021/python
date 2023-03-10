from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

client = MongoClient("localhost", 27017 )
db = client.Northwind
collection = db.Customers
cursor = collection.find({"Country":{"$eq" : "Mexico"}})

while (cursor.alive):
    d = cursor.next()
    print(d['CustomerID'])
    print(d['ContactName'])
    cursorPedidos = db.Orders.find({"CustomerID":d['CustomerID']})
    while (cursorPedidos.alive):
        c = cursorPedidos.next()
        print(c['OrderID'],c['OrderDate'])
    print("_______________________________________")


