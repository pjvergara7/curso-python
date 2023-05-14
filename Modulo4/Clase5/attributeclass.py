class Student:
    escuela_nombre = 'USACH'

    def __init__(self, _name, _age):
        self.name = _name
        self.asge = _age

    @classmethod
    def cambiar_escuela(cls, _new_name):
        cls.escuela_nombre = _new_name
    
    def ver_nombre_escuela(self):
        print(Student.escuela_nombre)

