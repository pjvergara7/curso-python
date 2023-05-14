class Empleado:
    sueldo = 0 #Variable de clase

    def __init__(self, _name):
        self.name = _name

persona = Empleado("miau miau")
print(persona.name)

#Hacer atributo name público, se redefine la clase
class EmpleadoProtected:
    sueldo = 0

    def __init__(self, _name) -> None:
        self.__name = _name

    @property   ##getter
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, _name):
        self.__name = _name

persona2 = EmpleadoProtected("Guau")
print(persona2.name)

persona2.name = "Tasmi"
print(persona2.name)