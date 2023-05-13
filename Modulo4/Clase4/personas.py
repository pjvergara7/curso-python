class Persona:
    def __init__(self, _rut, _nombre, _genero):
        self.rut = _rut
        self.nombre = _nombre
        self.genero = _genero

class Maestro(Persona):
    def __init__(self, _rut, _nombre, _genero, _clases_dictadas):
        super().__init__(_rut, _nombre, _genero)
        self.clases_dictadas = _clases_dictadas

class Estudiante(Persona):
    def __init__(self, _rut, _nombre, _genero, _numero_alumno, _clases_tomadas):
        super().__init__(_rut, _nombre, _genero)
        self.numero_alumno = _numero_alumno
        self.clases_tomadas = _clases_tomadas

class Universitario(Estudiante):
    def __init__(self, _rut, _nombre, _genero, _numero_alumno, _clases_tomadas, _carrera, _anio_carrera):
        super().__init__(_rut, _nombre, _genero, _numero_alumno, _clases_tomadas)
        self.carrera = _carrera
        self.anio_carrera = _anio_carrera