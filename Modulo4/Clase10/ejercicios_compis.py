class RevertirCadena:
    def __init__(self, _cadena):
        self.cadena = _cadena

    def revertir(self):
        palabras = self.cadena.split()
        palabras_reverse = palabras[::-1]
        cadena_reverse = ' '.join(palabras_reverse)
        return cadena_reverse
    
_cadena = input("Ingrese una frase: ")
reversor = RevertirCadena(_cadena)
print(reversor.revertir())
