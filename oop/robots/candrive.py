# для роботов роверов  
class CanDrive():
    
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.number_of_wheels}")'  
              
    @property
    def can_drive(self):
        print("могу ехать ")    

    



