class Persona:
    def __init__(self, _name) -> None:
        self.name = _name

    def test_error(self):
        try:
            result = 1 / self.name
        except TypeError:
            print("Hubo un error al intentar la operacion")

richar = Persona("Richar Lujano")
richar.test_error()