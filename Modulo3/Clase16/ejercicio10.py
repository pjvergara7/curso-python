numerador = float(input("Ingresa el primer número: "))
denominador = float(input("Ingresa el segundo número: "))
if denominador == 0:
    print("No se puede realizar la operación, el denominador debe ser distinto de cero")
else:
    resultado = numerador/denominador
    print(resultado)