lista_nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", 
                 "Messi", "Teller", "Einstein", "Pele", "Juanes"]

lista_magos = ["Harry Houdini", "David Blaine", "Teller"]
lista_100tificos = ["Newton", "Hawking", "Einstein"]
lista_otros = ["Messi", "Pele", "Juanes"]



def hacer_grandioso(lista):
    for i in range(len(lista)):
        lista[i] = 'El gran ' + lista[i]

def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)

print("Lista de nombres antes de modificar: ")
imprimir_nombres(lista_nombres)

print("Lista de nombres después de modificar: ")
hacer_grandioso(lista_magos)
imprimir_nombres(lista_magos)
imprimir_nombres(lista_100tificos)
imprimir_nombres(lista_otros)
