#utilizamos [] para crear listas
vacia = []
colores = ["naranja","rojo","amarillo","azul","verde"]

# Mostrar contenido de una lista
print(colores)

# Mostrar el valor contenido en una posicion
print(colores[3])

# Mostrar el numero de valores que contiene la lista 
print(len(colores))

# Mostrar el numero de veces que tenemos un valor 
print(colores.count("morado"))

# Modificar el valor de una posicion 
colores[2]="rosado"
print(colores)
print(colores[2])

# Añadir nuevos valores ultilizando la funcion APPEND
# APPEND añade en la ultima posicion
colores.append("negro")
colores.append("blanco")

# Añadir si el valor no existe
if ("dorado" not in colores):
    colores.append("dorado")

# Añadir varios valores que se encuentren en una lista con EXTEND(value)
nuevosColores = ["beige","gris","platiado"]
colores.extend(nuevosColores)

# Añadir un nuevo valor en una posicion especifica
colores.insert(3,"marron")

# Eliminar un valor en base a la posicion utilizando POP(index)
colores.pop(5)

# Eliminar un valor en base al valor utilizando REMOVE(value)
colores.remove("rojo")

# Eliminar un valor si existe 
if ("azul" in colores):
    colores.remove("azul")

# Invertir el orden de los valores utilizando REVERSE
colores.reverse()

# Ordenar los valores utilizando SORT
colores.sort()
colores.sort(reverse = True)

# Recorremos la lista y mostramos los valores
print("")
for color in colores:
    print(color)

for color in range(1, len(colores),1):
    print(color,": ", colores[color])

# Copiar todos los valores de la lista
lista2 = colores.copy()

# Eliminar todos los valores de la lista
colores.clear()


print(colores)