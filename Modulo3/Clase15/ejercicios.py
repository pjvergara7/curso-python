#contar letras en una frase
frase = input("Ingrese una frase o palabra: ")
letra = input("Ingrese letra a buscar: ")

print(f"La cantidad de '{letra}' es: {frase.count(letra)}")

#dado un capital K, a un interés Y (que va de 0 a 100), durante Z años y se desea saber cuánto se va a ahorrar sabiendo que es acumulativo
capital_i = float(input("Ingrese el monto a invertir: "))
interes = float(input("Ingrese la tasa de interés: "))
tiempo = int(input("Ingrese la cantidad de años: "))
capital_final = capital_i*(1 + interes)^tiempo
print("El valor acumulado final es ", capital_final)