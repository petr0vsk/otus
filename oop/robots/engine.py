from dataclasses import dataclass

@dataclass
class Engine:
    """ Датакласс для двигателей роботов """
    type: str = "base engine"
    engine_power: float = 20 # мощность двигателя
    fuel_rate:    float = 10 # расход топлива на 100 км 


base_engine = Engine()
hi_power_engine = Engine('high power engine', 200, 50)
aviation_engine = Engine('aviation_engine', 100, 45)
marine_engine =   Engine('marine_engine', 150, 25) 

