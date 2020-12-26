from abc import ABCMeta, abstractmethod
class FatherBot(object, metaclass=ABCMeta):
    def __init__(self, model, manufacture):
        self.model = model                  # модель
        self.manufacture = manufacture      # производитель

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.model}", {self.manufacture})'    

    @abstractmethod
    def check_fuel(self):                   # обязательная проверка в дочерних классах есть ли топливо в баке
        pass
    @property    
    def model(self):
        return self.__model
    @model.setter
    def model(self, new_model):
        if not isinstance(new_model, str):
            raise ValueError('Модель робота должна быть строковым значением')
        self.__model = new_model
    @property
    def manufacture(self):
        return self.__manufacture
    @manufacture.setter
    def manufacture(self, new_manufacture):
        if not isinstance(new_manufacture, str):
            raise ValueError('Завод-изготовитель должен быть строковым значением')
        self.__manufacture = new_manufacture    