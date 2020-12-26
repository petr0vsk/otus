# робот-амфибия. умеет плавать и летать.

from .fatherbot import FatherBot
from .bot import Bot
from .canfloat import CanFloat
from .canfly import  CanFly
class FlyingBoatBot(Bot, CanFloat, CanFly):
    def __init__(self, model, manufacture, name, weight, engine_power, fuel_supply, fuel_rate, displacement, number_of_wings):
        FatherBot.__init__(self, model, manufacture)
        Bot.__init__(self, model, manufacture, name, weight, engine_power, fuel_supply, fuel_rate)
        CanFloat.__init__(self, displacement) 
        CanFly.__init__(self, number_of_wings)


    def __repr__(self):
        return f'{self.__class__.__name__}("{self.model, self.manufacture, self.name, self.weight, self.engine_power, self.fuel_supply, self.fuel_rate, self.displacement, self.number_of_wings})' 

    @property
    def get_capability(self):                           # самореклама - а я еще могу ...
        print(f"Возможности: ", self.__repr__)
    