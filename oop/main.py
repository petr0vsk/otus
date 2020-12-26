from robots import Bot, RoverBot


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


r = RoverBot('RobotName', 'USRobotsInc', 'Name', 110, 10, 1000, 25, 4)
r.get_capability
r.power_to_weight
r.can_drive