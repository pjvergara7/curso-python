class SumaTres:
    def __init__(self, _numeros):
        self.numeros = _numeros

    def encontrar_suma_cero(self):
        for numero in self.numeros:
            try:
                float(numero)
            except ValueError:
                raise TypeError("La lista debe contener solo números enteros y reales.")

        resultados = []
        for i in range(len(self.numeros) - 2):
            for j in range(i + 1, len(self.numeros) - 1):
                for k in range(j + 1, len(self.numeros)):
                    if self.numeros[i] + self.numeros[j] + self.numeros[k] == 0:
                        resultados.append([self.numeros[i], self.numeros[j], self.numeros[k]])

        return resultados

try:
    lista_numeros = []
    cantidad = int(input('ingrese cantidad de números a combinar: '))
    for x in range(cantidad):
        numero = int(input('ingrese numero: '))
        lista_numeros.append(numero)
    
    suma_tres = SumaTres(lista_numeros)
    resultados = suma_tres.encontrar_suma_cero()

    if resultados:
        print("Las combinaciones de tres números que suman cero son:")
        for resultado in resultados:
            print(resultado)
    else:
        print("No se encontraron combinaciones de tres números que sumen cero.")
except ValueError:
    print("Asegúrate de ingresar solo números enteros.")