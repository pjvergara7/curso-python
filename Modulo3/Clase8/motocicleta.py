class Motocicleta():
    is_new = True
    motor = False

def __init__(self, _color, _matricula, _combustible_litros, _numero_ruedas,
    _marca, _modelo, _fecha_fabricacion, _velocidad_punta, _peso):
    self.color = _color
    self.matricula = _matricula
    self.combustible_litros = _combustible_litros
    self.numero_ruedas = _numero_ruedas
    self.marca = _marca
    self.modelo = _modelo
    self.fecha_fabricacion = _fecha_fabricacion
    self.velocidad_punta = _velocidad_punta
    self.peso = _peso

def arrancar(self):
    if self.motor == False:
        print("El motor ya estaba encendido")
    else:
        print("El motor ha arrancado")

def detener(self):
    if not self.motor:  #equivalente a self.motor == False
        print("El motor ya estaba detenido")
    else:
        print("El motor se ha apagado")

def consultar_precio(self):
    print(f"El precio de la motocicleta {self.marca} es de {self.precio}$")

#instanciamos una moto
moto1 = Motocicleta("Negro", "XX22", 10, 2, "Kawasaki", "Ninja", "03/10/2023",200, 120)
moto2 = Motocicleta(_color = "Azul",_matricula = "M0t013",
                    _combustible_litros = 15, _numero_ruedas = 2,
                    _marca = "Motomami", _modelo = "Rosalia",
                    _fecha_fabricacion = "18-03-2022", _velocidad_punta = 210,
                    _peso = 185)
moto3 = Motocicleta(_matricula="XXX-126", _combustible_litros=0, _color="Negra",
                    _marca="ZONTES", _modelo="V-310", _numero_ruedas=2, _peso=150,
                    _fecha_fabricacion="19/09/2023", _velocidad_punta=150)

moto2.arrancar()
moto1.detener()
moto1.precio = 9000
print(f"El precio de la motocicleta {moto1.marca} es de {moto1.precio}$")
moto1.consultar_precio()