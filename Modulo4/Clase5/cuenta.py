class Cuenta:
    def __init__(self, _titular, _cantidad) -> None:
        self.titular = _titular
        self.cantidad = _cantidad

    def imprimir(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad de dinero: {self.cantidad}")

class PlazoFijo(Cuenta):
    def __init__(self, _titular, _cantidad, _plazo, _interes):
        super().__init__(_titular, _cantidad)
        self.plazo = _plazo
        self.interes = _interes
    
    def importeInteres(self):
        importe = self.cantidad*self.interes*1/100
        return importe
    
    def mostrarInformacion(self):
        print(f"Titular: {self.titular}")
        print(f"Plazo: {self.plazo}")
        print(f"Interés: {self.interes}")
        print(f"Tasa de interés: {self.importeInteres}")

        
class CajaAhorro(Cuenta):
    def __init__(self, _titular, _cantidad):
        super().__init__(_titular, _cantidad)
    
    def herencia(self):
        print("herencia")

    def imprimeDatos(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad de dinero: {self.cantidad}")


cuenta1 = PlazoFijo("titular1", 120000, 5, 0.8)
cuenta2 = CajaAhorro("titular2", 150000)

cuenta1.mostrarInformacion
cuenta2.imprimeDatos