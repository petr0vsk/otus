# для роботов роверов  
class CanDrive():
    
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.number_of_wheels}")'  

    @property
    def number_of_wheels(self):
        return self.__number_of_wheels

    @number_of_wheels.setter
    def number_of_wheels(self, new_number_of_wheels):
        if not isinstance(new_number_of_wheels, int ):
                raise ValueError('Количество колесь рбота принадлежит к типу int')
        self.__number_of_wheels = new_number_of_wheels


    @property
    def can_drive(self):
        print("могу ехать ")    

    


