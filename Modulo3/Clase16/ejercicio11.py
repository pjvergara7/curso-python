def tributar(anios, ingreso):
    edad_minima = 16
    ingreso_tope = 1000
    if anios > edad_minima and ingreso >= ingreso_tope:
        print("Debe pagar impuestos")
    else:
        print("No paga impuesto")

anios = int(input("Ingresa tu edad: "))
ingreso = float(input("Ingresa tus ganancias mensuales: "))
tributar(anios,ingreso)