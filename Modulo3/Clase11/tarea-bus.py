#se necesita realizar un programa basado en clases que permita automatizar el torniquete 
#(control de acceso) de una micro, de la siguiente manera

#    1 Las personas que aboradan la micro son, mujeres, hombres, niños y aduto mayor, de los 
#cuales los niños no pagan y lso adultos mayores pagan la tarifa el 50%
      
#    2 el cobro actual de la micro es de 730 pesos

#    3 por lo que necesitamos un reporte de operacion por dia donde, por micro (cada micro 
#se reguistra por patente), se listen los tipos de usuario y la cantidad total recaudad por 
#cada, anexar a este reporte el total por dia

#    4. seria interesante que apart6e del reporte anterior que estotal, tener uno filtrado 
#por dia y otro filtrado por persona
from datetime import datetime

class Bus:
    def __init__(self):
        self.pasajeros = [] 
        self.accesos = []
        self.patentes = []
        self.valores_pasajeros = {
            'mujer': 730, 
            'hombre': 730, 
            'niño': 0, 
            'adulto': 730/2
            }

    def agregar_bus(self, _patente):
        self.patentes.append({
            'numero_patente': _patente,
            'correlativo_movimiento': 1
        })

    def agregar_pasajero(self, _tipo_pasajero, _patente):
        for elemento in self.patentes:
            if elemento['numero_patente'] == _patente:
                self.accesos.append({
                    'numero_patente': _patente,
                    'correlativo_movimiento': elemento['correlativo_movimiento'],
                    'fecha': datetime.today().strftime('%Y-%m-%d'),
                    'tipo_pasajero': _tipo_pasajero,
                    'valor': self.valores_pasajeros[_tipo_pasajero]
                })
                elemento['correlativo_movimiento'] += 1
                break
    
    def generar_reporte_diario(self, _patente):
        fecha = datetime.today().strftime('%Y-%m-%d')
        total_pasajeros = 0
        total_recaudado = 0
        for acceso in self.accesos:
            if acceso['numero_patente'] == _patente:
                print('Estoy entrando aquí')
                total_pasajeros += 1
                total_recaudado += acceso['valor']
        print(f"Reporte diario para el bus con patente {self.patentes[0]['numero_patente']}:")
        print(f"Fecha: {fecha}")
        print(f"Total de pasajeros: {total_pasajeros}")
        print(f"Total recaudado: {total_recaudado}")



bus_1 = Bus()

bus_1.agregar_bus('XXYY01')

bus_1.agregar_pasajero('XXYY01', 'adulto mujer')
bus_1.agregar_pasajero('XXYY01', 'adulto hombre')
bus_1.agregar_pasajero('XXYY01', 'adulto niño')
bus_1.agregar_pasajero('XXYY01', 'adulto mayor')

bus_1.generar_reporte_diario('XXYY01')