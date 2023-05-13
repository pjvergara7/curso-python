class Padre:
    def __init__(self, _name_padre, _rut_padre):
        self.name = _name_padre
        self.rut = _rut_padre
        self.sueldo = 0

    def pintar(self):
        print("Estoy pintando")

class Hijo(Padre):
    def __init__(self, _name_hijo, _rut_hijo, _color_ojos):
        Padre.__init__(self, _name_hijo, _rut_hijo)
        self.color_ojos = _color_ojos

    def lijar(self):
        print("Estoy lijando")
    
Frida = Padre("Frida miau", "111")
Sherlock = Hijo ("Sherlock", "222", "Naranjo")
print(Frida.name, Frida.sueldo)
print(Sherlock.name, Sherlock.sueldo)

Frida.pintar()
Sherlock.pintar()
Sherlock.lijar()