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