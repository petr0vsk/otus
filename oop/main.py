from robots import Bot, RoverBot, FlyingBoatBot

# робот без вожмности передвигаться
b = Bot('FirstModel', 'USRobotsInc', 'Name', 100, 10, 1000, 25)
#print(b.__repr__)
b.check_fuel
# удельная мощность при весе = 100 и мощности мотора 10
b.power_to_weight
# удельная мощность при весе = 200 и мощности мотора 50
b.weight = 200
b.engine_power = 50
b.power_to_weight
b.get_capability

# наземный робот вездеход
r = RoverBot('Model#12345', 'Boston Dynamics', 'BumblBee', 110, 10, 1000, 25, 4)
r.get_capability
r.power_to_weight
r.can_drive
print(r.number_of_wheels)
r.number_of_wheels = 8 
print(r.number_of_wheels)

# робот летающая лодка
c = FlyingBoatBot('Model#Catalina', 'USRobotics', 'SeaCat', 110, 10, 1000, 2500, 2666.8, 2)
c.get_capability
c.can_fly
c.can_float
c.check_fuel
print(c.number_of_wings)
