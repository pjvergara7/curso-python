def jugueteria(pay, mun):
    peso_payaso = 112
    peso_muneca = 75
    peso_total = peso_payaso*pay + peso_muneca*mun
    return peso_total

pay = int(input("Ingrese la cantidad de payasos a enviar en el paquete: "))
mun = int(input("Ingrese la cantidad de muñecas a enviar en el paquete: "))
print(f"El peso del paquete es: ", jugueteria(pay,mun))
