
from tortoise.models import Model
from tortoise import fields, Tortoise

class Weather(Model):
    """
    описывает погоду в городе:
    name:название_города, temp:температура F, pressure:давление, humidity:влажность 
    """
    id   = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    temp = fields.FloatField() 
    pressure = fields.FloatField() 
    humidity = fields.FloatField()

    class Meta:
        table = "weather" 

    def __str__(self):
        return f"{self.__class__.__name__} name:{self.name}, id: {self.id}, temp:{self.temp}, pressure:{self.pressure}, humidity: {self.humidity}"

    def __repr__(self):
        return self.__str__()
