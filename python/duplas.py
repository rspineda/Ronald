dupla1=("Ronald", 11, "Madrid")

#imp, recordar que no se pueden modificar los elementos de las duplas, tal como se hace en las lista, introduciendo nuevo elementos....

#acceso a un elemento:
print(dupla1[1])

#conversion de dupla en lista con "list"
lista1=list(dupla1)
print(dupla1)
print(lista1)

#conversion de lista en dupla con "tuple"
lista2=["Stevens", 12, "España"]
dupla2=tuple(lista2)
print(dupla2)

#para comprobar si un elemento esytá dentro de la tupla. Con "in", devuelve tru or false
print("Ronald" in dupla1)
print("########")
print("Ronald" in dupla2)

#para contar cuantas veces se encuentra un elemento en la dupla:
dupla3=("Ronald", 11, 12, "Amsterdam", "Madrid", "Amsterdam",11)
print(dupla3.count("Amsterdam"))
print("########")
print(dupla3.count(11))

#para saber la longitud de la dupla. Con "len"
print(len(dupla3))

#para crear una dupla unitaria(con un unico elemento)
dupla4=("Ronnie",)  #imp poner la coma
print(len(dupla4))

#ojo, que los parentesis son opcionales en la dupla: (empaquetado de tupla)
dupla5="Ronald", 11, "Madrid"
print(dupla5)

#desempaquetado de tupla
dupla6=("ronald", 11, "madrid")
nombre, dia, ciudad=dupla6  #en este caso se asigna cada variable a cada elemento de la dupla
print(nombre)
print(dia)
