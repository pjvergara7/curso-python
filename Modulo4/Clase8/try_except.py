## Sintaxis try except
## try
##      codigo
##      codigo
##      ......
## except ExceptionName
##      codigo
##      codigo
##      ......


dividendo = 100
while True:
    try:
        edad = int(input("Introduce tu edad: "))
        result = dividendo / edad
        break
    except ValueError as error:
        print("debe de colocar una edad valida")
        print(type(error))
        print(error.args)
        print(error)
    except ZeroDivisionError as error:
        print(type(error))
        print(error.args)
        print(error)


# Generar en difrentes class, al menos una clase por error, las siguientes Exceptions
# IndexError
# TypeError
# KeyError