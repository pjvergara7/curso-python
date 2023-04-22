print("====p1=====")
p1 = float(input("Ingrese puntaje 1, con formato decimal (por ej: 1.0): "))
p2 = float(input("Ingrese puntaje 2, con formato decimal (por ej: 1.0): "))
p3 = float(input("Ingrese puntaje 3, con formato decimal (por ej: 1.0): "))

promedio = (p1 + p2 + p3)/3
if promedio < 2:
    print("la calificación es D")
elif promedio > 2.1 and promedio < 5:
    print("la calificación es C")
elif promedio > 5.1 and promedio < 6:
    print("la calificación es B")
else:
    print("la calificación es A")

print("====p2=====")
max = int(input("Escribe la cantidad de números que quieres construir de la tabla de multiplicar (debe ser un número entero): "))
cont = 1
iter = 1
while cont <= 10 and iter <= max:
    cont2 = 1
    while cont2 <= 10 and iter <= max:
        print(cont, "*", cont2, "=", cont*cont2)
        cont2 += 1
    cont += 1
    iter += 1

print("====p3=====")
num1 = int(input("Ingrese el primer número (debe ser entero y distinto de 0) para calcular el m.c.m. \n"))
num2 = int(input("Ingrese el segundo número (debe ser entero y distinto de 0) para calcular el m.c.m. \n"))
while num2 != 0:
    resto = num1%num2
    num1 = num2
    num2 = resto
print("El m.c.m. es: ", num1)

print("====p4=====")
mes = int(input("Ingrese el número del mes del año (1 al 12) para saber en qué trimestre se encuentra \n"))
if mes > 0 and mes < 12:
    if mes/3 <= 1:
        print("El mes forma parte del primer trimestre")
    elif mes/3 > 1 and mes/3 <= 2:
        print("El mes forma parte del segundo trimestre")
    elif mes/3 > 2 and mes/3 <= 3:
        print("El mes forma parte del tercer trimestre")
    elif mes/3 > 3 and mes/3 <= 4:
        print("El mes forma parte del cuarto trimestre")

print("====p5=====")
cadena = input("Ingrese oración con signo de exclamación al final \n")
cadena_a_lista = list(cadena)
cadena_sin_signo = cadena_a_lista.pop()
cadena_final = "".join(cadena_a_lista)
print("La cadena sin el signo es: ", cadena_final)

print("====p6=====")
carga_lavadora = int(input("Ingresa la capacidad de carga de la lavadora (en número entero y kg): \n"))
tipo_ropa = input("Ingresa el tipo de material de la ropa (algodón, nylon o poliéster) \n")
if carga_lavadora > 0:
    if tipo_ropa == "algodón":
        x = carga_lavadora*50/7 + 5
    elif tipo_ropa == "nylon":
        x = carga_lavadora*50/7 + 1
    elif tipo_ropa == "poliéster":
        x = carga_lavadora*50/7 + 3

print("Se necesita ", x, " litros de agua para lavar la ropa")

print("====p7=====")
nota_ex = float(input("Ingrese la nota que obtuvo en el examen (del 1 al 100): \n"))
cant_proyectos = int(input("Ingrese la cantidad de proyectos desarrollados (debe ser número entero): \n"))
if nota_ex > 90 or cant_proyectos > 10:
    final = 100
elif (nota_ex >= 75 and nota_ex < 90) or (cant_proyectos >= 5 and cant_proyectos <= 10):
    final = 90
elif (nota_ex >= 50 and nota_ex < 75) or (cant_proyectos >= 2 and cant_proyectos < 5):
    final = 75
print("La calificación final es: ", final)