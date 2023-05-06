def impuestos(renta):
    if renta < 10000:
        print("Debe pagar un impuesto del 5%")
    elif renta < 20000 and renta >= 10000:
        print("Debe oagar un impuesto del 15%")
    elif renta < 35000 and renta >= 20000:
        print("Debe oagar un impuesto del 20%")
    elif renta <= 60000 and renta >= 35000:
        print("Debe oagar un impuesto del 30%")
    else:
        print("Debe pagar un impuesto de 45%")

renta_anual = float(input("Ingrese su renta anual en miles de euros, puede usar decimales: "))
impuestos(renta_anual)