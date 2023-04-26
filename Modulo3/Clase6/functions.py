def saludar(name):
    print(f"Hola {name}!!!")

def saludar2(first_name, last_name):
    print(f"Hola {first_name}, {last_name}!!!")

saludar("Rodrigo")

saludar2("Paulina", "Vergara")

def multiplicar_texto(texto, multiplier = 2):
    print(texto*multiplier)

multiplicar_texto("Miau")
multiplicar_texto("guau", 5)

def varietal_dos(param1, **others):
    print(param1)
    print(others)

print("\n --------------------- \n")
varietal_dos("miau", id = 0, name = "Tas")
