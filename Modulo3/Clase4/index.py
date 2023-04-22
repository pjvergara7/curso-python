print("==========Trabajo con diccionarios============")

empty_dict = {}

fullfilled_dict = {
    "id": 1,
    "name": "Valeria"
}

print(empty_dict)
print(fullfilled_dict)

lista_1 = ["a1", "b2"]
dict_converted = dict(lista_1)
print(lista_1, dict_converted)

tupla_1 = ("a2", "b1")
print(tupla_1,dict(tupla_1))

list_dimension1 = [["a", 1], ["b", 3]]
print(list_dimension1, dict(list_dimension1))

diccionario = {5:"anillo", 2:"gato", 3:"doggo"}
print(diccionario)

diccionario[4] = "cuaderno"
print(diccionario)

print(diccionario[5])

empty_dict2 = dict()
print(empty_dict2)

full_dict = dict(
    genero = "H",
    nacionalidad = "t"
)
print(full_dict)

empleado = {
    "name": "Valeria",
    "apellido": "Rosso",
    "edad": 18,
    "rut": "11.112.568-9"
}
print(empleado)

for variablex in empleado.values():
    print(variablex)

for clave,valor in empleado.items():
    print(clave,valor)


print("===========Ahora vamos con condicionales========")

edad = 50
if edad > 45:
    print("Hola caballero")

print("continuamos el código")

temperatura = 30
if temperatura <= 24:
    print("Temperatura agradable")
else:
    print("Temperatura desagradable :C")

temperatura2 = 5
pais = "Chile"

if temperatura <5:
    if pais == "Chile":
        print("yey")
    else:
        print("Oh :(")
else:
    if pais == "Chile":
        print("miau")
    else:
        print("guau")

print("========Ciclos: While========")

want_exit = False
while want_exit == False:
    print("hola cómo te va?")
    pregunta = input("¿Quieres terminar el ciclo? T para sí, F para no \n")
    if pregunta == "T":
        want_exit = True
    else:
        want_exit = False
print("Fuera del while")

print("========Ciclos: While2========")
want_exit = "T"
numero = 0
while want_exit == False:
    print("hola cómo te va?")
    want_exit = input("¿Quieres terminar el ciclo? T para sí, F para no \n")
    numero += 1
    if numero == 4:
        print("ya no puedes entrar más al while")
        break
print("Fuera del while yeeey")