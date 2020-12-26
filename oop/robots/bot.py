from pprint import pprint
from .fatherbot import FatherBot  

class Bot(FatherBot):
    def __init__(self, model, manufacture, name, weight, engine_power, fuel_supply, fuel_rate):
        #FatherBot.__init__(self, model, manufacture)
        super().__init__(model, manufacture)
        self.name = name                        # имя робота
        self.weight = weight                    # вес
        self.engine_power = engine_power        # мощность двигателя
        self.fuel_supply = fuel_supply          # запас топлива
        self.fuel_rate = fuel_rate              # расход топлива на 100 км
        self.__spec_engin_power = None          # если еще не вычисляли spec_engin_power

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.model, self.manufacture, self.name,  self.weight, self.engine_power, self.fuel_supply, self.fuel_rate})'    

    @property
    def check_fuel(self):                       # проверка остатка топлива
        if self.fuel_supply <= 0:
            raise ValueError("Топливо закончилось, ищем гравицапу!")
        else:
            print(f"Можем ехать, мощность топливных элементов = {self.fuel_supply}")
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
    def engine_power(self):
        return self.__engine_power

    @engine_power.setter                            # при изменении мощности вызовем пересчет удельной мощности 
    def engine_power(self, new_engine_power):
        if not isinstance(new_engine_power, int):
                raise ValueError('Имя робота должно быть строковым значением')
        self.__engine_power = new_engine_power
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
    def fuel_rate(self):
        return self.__fuel_rate

    @fuel_rate.setter
    def fuel_rate(self, new_fuel_rate):    
        if not isinstance(new_fuel_rate, int):
                raise ValueError('Расход топлива должен быть int')
        self.__fuel_rate = new_fuel_rate    

    @property
    def power_to_weight(self):                          # вычисление удельной мощности движка 
        if self.__spec_engin_power is None:             # если еще не вычисляли spec_engin_power
            spec_engin_power = self.__weight / self.__engine_power
            print(f"Удельная мощность двигателя {spec_engin_power}") 
        return spec_engin_power

    @property
    def get_capability(self):                           # самореклама - а я еще могу ...
        print(f"Возможности: ", self.__repr__)
