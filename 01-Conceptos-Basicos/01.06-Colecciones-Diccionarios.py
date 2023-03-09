# Utilizamos {} para crear un diccionario
# FUNCIONES ()
# COLECCIONES []
# DICCIONARIOS {}
vacia = {}
colores = {"NA":"naranja" , "RO":"rojo" , "AM":"amarillo" , "AZ":"azul" , "VE":"verde"}

# Mostrar el diccionario 
print(colores)

# Mostrar un valor utilizando la key(clave)
# Si la clave no existe se genera un Exception
print(colores["NA"])

# Mostra un valor utilizando la funcion GET
# Si la clave no existe, la funcion GET retorna el valor None
print(colores.get("NA"))
print(colores.get("JE"))

# Mostrar el numero de valores del diccionario
print(len(colores))

# Modificar el valor del diccionario
colores["RO"] = "rosado"
print(colores["RO"])

# Añadir un nuevo valor al diccionario
colores["NE"]="negro"

# Eliminar un valor utiliznado la clave
colores.pop("AM")
del colores["VE"]

# Recorremos y mostramos todos los valores del diccionario utilizando FOR
for key in colores:
    print(f"Calve:{key} - Valor:{colores[key]}")

print(colores)