class Vehiculo:
    def __init__(self, marca, modelo, anio_fabricacion, motor, tipo_combustible, tipo_automovil, valor, num_puertas, num_asientos, velocidad_maxima, color, tipo_carga=None, volumen_carga=None):
        self.marca = marca
        self.modelo = modelo
        self.anio_fabricacion = anio_fabricacion
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.valor = valor
        self.num_puertas = num_puertas
        self.num_asientos = num_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.tipo_carga = tipo_carga
        self.volumen_carga = volumen_carga

class Propietario:
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut

class Policia:
    def __init__(self, nombre):
        self.nombre = nombre
        ##agregar rut

class Multa:
    def __init__(self, vehiculo, propietario, policia, fecha, monto):
        self.vehiculo = vehiculo
        self.propietario = propietario    ##se puede heredar desde vehiculo
        self.policia = policia
        self.fecha = fecha
        self.monto = monto

class Comuna:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos = []
        self.propietarios = []
        self.policias = []
        self.multas = []

    def registrar_vehiculo(self):
        marca = input("Marca del vehículo: ")
        modelo = input("Modelo del vehículo: ")
        anio_fabricacion = int(input("Año de fabricación del vehículo: "))
        motor = float(input("Volumen en litros del motor: "))
        tipo_combustible = input("Tipo de combustible: ")
        tipo_automovil = input("Tipo de automóvil: ")
        valor = float(input("Valor del vehículo: "))
        num_puertas = int(input("Número de puertas: "))
        num_asientos = int(input("Cantidad de asientos: "))
        velocidad_maxima = float(input("Velocidad máxima: "))
        color = input("Color del vehículo: ")
        tipo_carga = input("Tipo de carga (opcional): ")
        volumen_carga = None
        try:
            volumen_carga = float(input("Volumen de carga (Kilogramos), ingresar solo números: "))
        except ValueError:
            print("Error: El volumen de carga debe ser un número válido.")

        vehiculo = Vehiculo(marca, modelo, anio_fabricacion, motor, tipo_combustible, tipo_automovil, valor, num_puertas, num_asientos, velocidad_maxima, color, tipo_carga, volumen_carga)
        self.vehiculos.append(vehiculo)

    def registrar_propietario(self):
        nombre = input("Nombre del propietario: ")
        rut = input("RUT del propietario: ")

        propietario = Propietario(nombre, rut)
        self.propietarios.append(propietario)

    def registrar_policia(self):
        nombre = input("Nombre del policía: ")

        policia = Policia(nombre)
        self.policias.append(policia)
        
    def registrar_multa(self):
        vehiculo = input("Ingrese la patente del vehículo: ")
        propietario = input("Ingrese el RUT del propietario: ")
        policia = input("Ingrese el nombre del policía: ")
        fecha = input("Ingrese la fecha de la multa (dd/mm/aaaa): ")
        monto = None
        try:
            monto = int(input("Ingrese el monto de la multa sin puntos: "))
        except ValueError:
            print("Error: El monto de la multa debe ser un número válido.")

        multa = Multa(vehiculo, propietario, policia, fecha, monto)
        self.multas.append(multa)

def consultar_multas_por_policia(self):
    policia = input("Ingrese el nombre del policía: ")
    fecha = input("Ingrese la fecha para filtrar las multas (dd/mm/aaaa): ")

    multas_policia = [multa for multa in self.multas if multa.policia == policia and multa.fecha == fecha]

    if multas_policia:
        for multa in multas_policia:
            print("Vehículo: ", multa.vehiculo)
            print("Propietario: ", multa.propietario)
            print("Fecha: ", multa.fecha)
            print("Monto: ", multa.monto)
            print("----")
    else:
        print("No se encontraron multas para el policía y la fecha especificada.")

def consultar_multas_por_vehiculo(self):
    vehiculo = input("Ingrese la patente del vehículo: ")

    multas_vehiculo = [multa for multa in self.multas if multa.vehiculo == vehiculo]

    if multas_vehiculo:
        for multa in multas_vehiculo:
            print("Vehículo: ", multa.vehiculo)
            print("Propietario: ", multa.propietario)
            print("Fecha: ", multa.fecha)
            print("Monto: ", multa.monto)
            print("----")
    else:
        print("No se encontraron multas para el vehículo especificado.")

def mostrar_menu():
    comuna = Comuna(input("Ingrese el nombre de la comuna: "))
    while True:
        print("\n-------- Menú --------")
        print("1. Registrar vehículo")
        print("2. Registrar propietario")
        print("3. Registrar policía")
        print("4. Registrar multa")
        print("5. Consultar multas por policía")
        print("6. Consultar multas por vehículo")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
          comuna.registrar_vehiculo()
        elif opcion == "2":
            comuna.registrar_propietario()
        elif opcion == "3":
            comuna.registrar_policia()
        elif opcion == "4":
            comuna.registrar_multa()
        elif opcion == "5":
            comuna.consultar_multas_por_policia()
        elif opcion == "6":
           comuna.consultar_multas_por_vehiculo()
        elif opcion == "0":
           break
        else:
           print("Opción inválida. Intente nuevamente.")

mostrar_menu()
