def banco(monto_inicial):
    interes = 0.04
    saldo_anio_1 = monto_inicial*interes + monto_inicial
    print(f"El saldo del primer año es: {saldo_anio_1:.2f}")
    saldo_anio_2 = saldo_anio_1*interes + saldo_anio_1
    print(f"El saldo del segundo año es: {saldo_anio_2:.2f}")
    saldo_anio_3 = saldo_anio_2*interes + saldo_anio_2
    print(f"El saldo del tercer año es: {saldo_anio_3:.2f}")

monto_inicial = float(input("Ingrese monto inicial: "))
banco(monto_inicial)