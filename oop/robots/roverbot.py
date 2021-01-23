from .fatherbot import FatherBot
from .bot import Bot
from .candrive import CanDrive
from  .engine     import Engine, base_engine, aviation_engine, marine_engine, hi_power_engine 
class RoverBot(Bot, CanDrive):
    """
    Робот для движения по поверхности планеты
    """
    def __init__(self, model, manufacture, name, weight, fuel_supply, engine, number_of_wheels):
        FatherBot.__init__(self, model, manufacture)
        Bot.__init__(self, model, manufacture, name, weight, fuel_supply, engine=base_engine)
        CanDrive.__init__(self, number_of_wheels)

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.model, self.manufacture, self.name, self.weight, self.fuel_supply, self.engine.type, self.number_of_wheels})' 
    
    @property
    def get_capability(self):                           # самореклама - а я еще могу ...
        print(f"Характеристики робота: ", self.__repr__)
        self.can_drive
