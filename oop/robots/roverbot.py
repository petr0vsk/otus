
from .fatherbot import FatherBot
from .bot import Bot
from .candrive import CanDrive
class RoverBot(Bot, CanDrive):
    def __init__(self, model, manufacture, name, weight, engine_power, fuel_supply, fuel_rate, number_of_wheels):
        FatherBot.__init__(self, model, manufacture)
        Bot.__init__(self, model, manufacture, name, weight, engine_power, fuel_supply, fuel_rate)
        CanDrive.__init__(self, number_of_wheels)

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.model, self.manufacture, self.name, self.weight, self.engine_power, self.fuel_supply, self.fuel_rate, self.number_of_wheels})' 