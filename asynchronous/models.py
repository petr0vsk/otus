from tortoise.models import Model
from tortoise import fields, Tortoise, run_async
import logging


class Weather(Model):
    """
    описывает погоду в городе,
    название_города, температура F, давление, влажность 
    """
    id       = fields.IntField(pk=True)
    datetime = fields.DatetimeField(auto_now_add=True)
    name     = fields.CharField(max_length=255)
    temp     = fields.FloatField() 
    pressure = fields.FloatField() 
    humidity = fields.FloatField()

    
    class Meta:
        table = "weather" 

    def __str__(self):
        return f"{self.__class__.__name__} id: {self.id}, datetime:{self.datetime},  name:{self.name},  temp:{self.temp}, pressure:{self.pressure}, humidity: {self.humidity}"

    def __repr__(self):
        return self.__str__()



