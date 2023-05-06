puntos = float(input("Ingrese los puntos obtenidos en la evaluación: "))
if puntos == 0.0:
    print("No recibirá dinero, su rendimiento es inaceptable")
elif puntos == 0.4:
    print("El puntaje obtenido lo ubica en un rendimiento aceptable, lo que significa que recibre un bono de 960 euros")
elif puntos >= 0.6:
    print("El puntaje obtenido lo ubica en un rendimiento meritorio, lo que significa que recibre un bono de 1440 euros")