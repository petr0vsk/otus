from abc import ABCMeta, abstractmethod
#---
class FatherBot(object, metaclass=ABCMeta):
    def __init__(self, model):
        self.model = model                  # модель робота
#-----       
class Bot(FatherBot):
    def __init__(self, model, name):
        #FatherBot.__init__(self, model)
        super().__init__(model)
        self.name = name                     # имя робота
    def __str__(self):
        return (f"Модель робота Bot - {b.model}, имя робота - {b.name}")
#------
class CanDrive():
    def __init__(self, number_of_wheels = 4):
        self.number_of_wheels = number_of_wheels
    def __str__(self):
        return (f"Количество колес CanDrive --  {self.number_of_wheels}")    
#-----
class RoverBot(Bot, CanDrive):
    def __init__(self, model, name, number_of_wheels, weight):
        #super().__init__(model, name)
        FatherBot.__init__(self, model)
        Bot.__init__(self, model, name)
        CanDrive.__init__(self, number_of_wheels)
        self.weight = weight
    def __str__(self):
        return (f"Модель робота RoverBot - {self.model}, имя робота - {self.name}, количество колес - {self.number_of_wheels}  вес - {self.weight}")


b = Bot("Model-1", "Name-1")       
print(b)
c = CanDrive()
print(c)
r = RoverBot("Model-2", "RoverName", 4, 222)
print(r)