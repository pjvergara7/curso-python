pizza_veg = ["pimiento", "tofu"]
pizza_nor = ["pepperoni", "jamón", "salmón"]
base_pizza = ["tomate", "mozzarella"]
tipo_pizza = input("¿Qué tipo de pizza desea? Las opciones son vegetariana o normal: ")
if tipo_pizza == "vegetariana" or tipo_pizza == "Vegetariana":
    print(pizza_veg)
    ingrediente = input("¿Qué ingrediente desea? ")
    base_pizza.append(ingrediente)
    print("Los ingredientes de la pizza son: ", base_pizza)
elif tipo_pizza == "normal" or tipo_pizza == "Normal":
    print(pizza_nor)
    ingrediente = input("¿Qué ingrediente desea? ")
    base_pizza.append(ingrediente)
    print("Los ingredientes de la pizza son: ", base_pizza)

