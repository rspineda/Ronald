miLista = ["Adriaan", "Ronald", "Alida", "Pelusa"]

print(miLista[2]) 

print(miLista[:]) #devuelve todos los elementos en un array, es decir el array entero

print(miLista[-2]) #devuelve el segundo elemento desde el final

print(miLista[0:3]) #devuelve trozos del array. En este caso desde la posición 0 hasta la 3, sin incluir las 3.

#el comando anterior tambien podría ser sin anotar el cero--> [:3]

print(miLista[1:3]) #devuelve desde el primer elemento hasta el 3, sin incluir al 3.

#print(miLista[2:]) devolvería desde el elemento 2 hasta el último


#agregando elemento al array
miLista.append("Locotona") # append agrega elemento al final, como push en javascript
print(miLista[:])

miLista.insert(1,"Gordotona") #insert agrega el elemento definiendo la posición deseada
print(miLista[:])

miLista.extend(["Helena", "Eduardo", "Felipe"]) #inserta un array entero al final de otro array
print(miLista[:])


#para que nos devuelva el índice o la posición de un array
print(miLista.index("Gordotona")) 

#para que devuelva true or false, en caso de que ese encuentre o no un elemento en la lista(array)
print("Francisco" in miLista) #devuelve true or false


#eliminando elementos
#remove elimina cualquier elemento deseado
miLista.remove("Helena") #como argumento recibe el elemento, siendo number , string, bolean....
print(miLista[:])

#pop() elimina el último elemento de la lista
miLista.pop()
print(miLista[:])

#Concatenando listas (arrays) y devolviendo una nueva lista que los engloba
miLista1 = ["Maripili", 23, "Jaén", True]
miLista2 = ["Juanito", 34, "Madrid", True ]
miLista3 = miLista1+miLista2

print(miLista3[:])

#repitiendo la lista un numero de veces
miLista4 = miLista1*3
print(miLista4[:])