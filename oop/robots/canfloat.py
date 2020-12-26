# для плавающих роботов 
class CanFloat():
    
    def __init__(self, displacement):
        self.displacement = displacement

    def __repr__(self):
         return f'{self.__class__.__name__}("{self.displacement}")'  

    @property
    def displacement(self):
        return self.__displacement

    @displacement.setter
    def displacement(self, new_displacement):
        if not isinstance(new_displacement, float ):
                raise ValueError('Водоизмещение принадлежит к типу flaot')
        self.__displacement = new_displacement


    @property
    def can_float(self):
        print("могу плыть")    