from pprint import pprint
from .fatherbot import FatherBot
from .engine import Engine, base_engine  
from .fuel_exception import LowFuelError

class Bot(FatherBot):
    """
    Базовый класс роботов без выбора способа передвижения
    """
    def __init__(self, model, manufacture, name, weight, fuel_supply, engine=base_engine):
        super().__init__(model, manufacture)
        self.name = name                        # имя робота
        self.weight = weight                    # вес
        self.fuel_supply = fuel_supply          # запас топлива
        self.engine = engine                    # двигатель из датакласса
        self.__spec_engin_power = None          # удельная мощность движка

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.model, self.manufacture, self.name,  self.weight,  self.fuel_supply, self.engine.type})'    

    @property
    def check_fuel(self):                       # проверка остатка топлива
        if self.fuel_supply <= 0:
            raise ValueError("Топливо закончилось, ищем гравицапу!")
        else:
            print(f"Запас топлива = {self.fuel_supply}")
            return self.fuel_supply

    @property 
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):    
        if not isinstance(new_name, str):
                raise ValueError('Имя робота должно быть строковым значением')
        self.__name = new_name

    @property
    def weight(self):
        return self.__weight

    @weight.setter                                 # при изменении веса вызовем пересчет удельной мощности 
    def weight(self, new_weight):
        if not isinstance(new_weight, int):
                raise ValueError('Вес робота должен быть int или float')
        self.__weight = new_weight
        self.__spec_engin_power = None   

    
    @property 
    def fuel_supply(self):
        return self.__fuel_supply

    @fuel_supply.setter
    def fuel_supply(self, new_fuel_supply):    
        if not isinstance(new_fuel_supply, int):
                raise ValueError('Запас топлива должен быть int')
        self.__fuel_supply = new_fuel_supply

    @property
    def power_to_weight(self):                          # вычисление удельной мощности движка 
        if self.__spec_engin_power is None:             # если еще не вычисляли spec_engin_power
            spec_engin_power = self.__weight / self.engine.engine_power
            #print(f"Удельная мощность двигателя {spec_engin_power}") 
            return spec_engin_power    

    
    @property
    def get_capability(self):                           # самореклама - а я еще могу ...
        print(f"Возможности: ", self.__repr__)

    def go_to(self, distance):                      # движение, при наличии топлива
        try:
            required_fuel_supply = distance *  self.engine.fuel_rate
            if required_fuel_supply > self.fuel_supply:
                delta_fuel = required_fuel_supply - self.fuel_supply
                raise LowFuelError(self.fuel_supply, delta_fuel)
            print("Топлива достаточно. Поехали!!!")
        except LowFuelError as err:
            print(f"Не могу выполнить команду. Запас топлива: {err.args[0]}, требуется добавить {err.args[1]}")        
