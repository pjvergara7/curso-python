class Artefacto:
    def __init__(self,name, color, peso):
        self.__name = name
        self.__color = color
        self.__peso = peso

    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name: str) -> None:
        self.__name =  name
    
    @property
    def color(self) -> str:
        return self.__color
    @color.setter
    def color(self, color: str) -> None:
        self.__color =  color

    @property
    def peso(self) -> float:
        return self.__peso
    @peso.setter
    def peso(self, peso: float) -> None:
        self.__peso =  peso


drone = Artefacto("Droni", "Gris", 4.4)
drone.color = "rosado"
print(drone.color)
print(drone)

