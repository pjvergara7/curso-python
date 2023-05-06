nombre = input("Ingresa tu nombre: ")
sexo = input("Ingresa tu sexo: ")
if ((sexo == "mujer" or sexo == "Mujer") and (nombre[0] == "A" or nombre[0] == "a" or nombre[0] == "B" or nombre[0] == "b" or nombre[0] == "C" or 
                                             nombre[0] == "c" or nombre[0] == "D" or nombre[0] == "d" or nombre[0] == "E" or nombre[0] == "e" or
                                             nombre[0] == "F" or nombre[0] == "f" or nombre[0] == "G" or nombre[0] == "g" or nombre[0] == "H" or 
                                             nombre[0] == "h" or nombre[0] == "I" or nombre[0] == "i" or nombre[0] == "J" or nombre[0] == "j" or
                                             nombre[0] == "K" or nombre[0] == "k" or nombre[0] == "L" or nombre[0] == "l")) or ((sexo == "hombre" or 
                                                                                                                                    sexo == "Hombre") and 
                                                                                                                                    (nombre[0] == "A" or 
                                                                                                                                     nombre[0] == "a" or 
                                                                                                                                     nombre[0] == "B" or 
                                                                                                                                     nombre[0] == "b" or 
                                                                                                                                     nombre[0] == "C" or
                                                                                                                                     nombre[0] == "c" or 
                                                                                                                                     nombre[0] == "D" or 
                                                                                                                                     nombre[0] == "d" or 
                                                                                                                                     nombre[0] == "E" or 
                                                                                                                                     nombre[0] == "e" or
                                                                                                                                     nombre[0] == "F" or 
                                                                                                                                     nombre[0] == "f" or 
                                                                                                                                     nombre[0] == "G" or 
                                                                                                                                     nombre[0] == "g" or 
                                                                                                                                     nombre[0] == "H" or 
                                                                                                                                     nombre[0] == "h" or 
                                                                                                                                     nombre[0] == "I" or 
                                                                                                                                     nombre[0] == "i" or 
                                                                                                                                     nombre[0] == "J" or 
                                                                                                                                     nombre[0] == "j" or 
                                                                                                                                     nombre[0] == "K" or 
                                                                                                                                     nombre[0] == "k" or 
                                                                                                                                     nombre[0] == "L" or 
                                                                                                                                     nombre[0] == "l")):
    print("Perteneces al grupo A")
else:
    print("Pertenece al grupo B")