from .fatherbot import FatherBot
from .bot import Bot
from .canfloat import CanFloat
from .canfly import  CanFly
from .engine import Engine, base_engine, aviation_engine, marine_engine, hi_power_engine 

class FlyingBoatBot(Bot, CanFloat, CanFly):
    """
    Класс робот летающая лодка
    """
    def __init__(self, model, manufacture, name, weight, fuel_supply, engine, displacement, number_of_wings):
        FatherBot.__init__(self, model, manufacture)
        Bot.__init__(self, model, manufacture, name, weight, fuel_supply, engine=aviation_engine)
        CanFloat.__init__(self, displacement) 
        CanFly.__init__(self, number_of_wings)


    def __repr__(self):
        return f'{self.__class__.__name__}("{self.model, self.manufacture, self.name, self.weight, self.fuel_supply, self.engine.type, self.displacement, self.number_of_wings})' 

    @property # возможности робота
    def get_capability(self):                           # самореклама - а я еще могу ...
        print(f"Характеристики робота: ", self.__repr__)
        self.can_fly
        self.can_float
            
