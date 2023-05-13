class Vehiculo:
    def __init__(self, _color, _ruedas, _tipo_freno, _tipo_bocina) -> None:
        self.color = _color
        self.ruedas = _ruedas
        self.tipo_freno = _tipo_freno
        self.tipo_bocina = _tipo_bocina

class Auto(Vehiculo):
    def __init__(self, _color, _ruedas, _tipo_freno, _tipo_bocina, _tipo_motor, _tipo_encendido, _caballos_fuerza):
        super().__init__(_color, _ruedas, _tipo_freno, _tipo_bocina)
        self.tipo_motor = _tipo_motor
        self.tipo_encendido = _tipo_encendido
        self.caballos_fuerza = _caballos_fuerza
        
class Moto(Vehiculo):
    def __init__(self, _color, _ruedas, _tipo_freno, _tipo_bocina, _tipo_motor, _tipo_encendido, _tipo_cadena, _tipo_amortiguador):
        super().__init__(_color, _ruedas, _tipo_freno, _tipo_bocina)
        self.tipo_motor = _tipo_motor
        self.tipo_encendido = _tipo_encendido
        self.tipo_cadena = _tipo_cadena
        self.tipo_amortiguador = _tipo_amortiguador

class Bicicleta(Vehiculo):
    def __init__(self, _color, _ruedas, _tipo_freno, _tipo_bocina, _tipo_manubrio, _tipo_material):
        super().__init__(_color, _ruedas, _tipo_freno, _tipo_bocina)
        self.tipo_manubrio = _tipo_manubrio
        self.tipo_material = _tipo_material
