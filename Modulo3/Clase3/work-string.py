first_name = "Miau"
last_name = "Meow"
print(first_name + " " + last_name)


variable = "Hola "*3
print(variable)

mensaje1 = "Tasmania"
print(mensaje1)
mensaje1 += ","
print(mensaje1)
mensaje1 += " siéntate"
print(mensaje1)

print(len(mensaje1))

cadena = "esto es una cadena de string"
posicion = cadena.find("pelo")
print("pelo se encuentra en: ", posicion)
posicion2 = cadena.find("string")
print("string se encuentra en: ", posicion2)


mensaje2 = "MIAU"
print(mensaje2.lower())

mensaje3 = "me gustan los gatos"
x = mensaje3.replace("gatos", "perros")
print(x)
print(mensaje3.replace("gatos", "hurones"))

print("========Listas==========")
empty_list = []
print(empty_list)

fullfilled_list = [1,3,5,7,9, [45, "jeje"], {"ñon": "nai"}, (2,4,6)]
print(fullfilled_list)

second_list = ()
print(second_list)
print(list("Concurso"))

range_one = range(50)
print(list(range_one))

numeros = [1,4,6]
print(numeros)
numeros.append(8)
print(numeros)

print(numeros[2])
print("Recorrer lista por Indices")
for x in range(0,len(numeros)):
    print(numeros[x])


elemento_eliminado = numeros.pop(2)
print("el elemento eliminado es: ", elemento_eliminado)
print(numeros)

eliminar_ultimo_elemto = numeros.pop()
print(numeros)


numeros.append(3)
numeros.append(34)
print(numeros)
numeros.remove(3)

del numeros[0]
print(numeros)
print(numeros.insert(1,12))