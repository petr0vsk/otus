# для летающих роботов 
class CanFly():
    """
    класс-миксин, дающий роботу возможность летать
    """
    def __init__(self, number_of_wings):
        self.number_of_wings = number_of_wings

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.number_of_wings}")'  

    @property
    def number_of_wings(self):
        return self.__number_of_wings

    @number_of_wings.setter
    def number_of_wings(self, new_number_of_wings):
        if not isinstance(new_number_of_wings, int ):
                raise ValueError('Количество крыльев рбота принадлежит к типу int')
        self.__number_of_wings = new_number_of_wings


    @property
    def can_fly(self):
        print("могу летать")    
