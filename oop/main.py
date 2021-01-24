from robots import Bot, RoverBot, FlyingBoatBot, Engine, hi_power_engine, aviation_engine
def main():
    # наземный робот вездеход
    print("======== Демонстрация возможностей робота-вездехода ============")
    rover = RoverBot('Model#12345', 'Boston Dynamics', 'BumblBee', 110, 10000, hi_power_engine, 4)
    print("Удельная мощность двигателя: ", rover.power_to_weight)
    print("Количество колес робота: ",rover.number_of_wheels)
    rover.number_of_wheels = 8 # проверим геттер по установке количества колес
    print("Количество колес робота: ",rover.number_of_wheels)
    rover.go_to(10)             # отправим робота в путь
    rover.get_capability        # получим возможности робота, перегрузка метода get_capability
    # робот летающая лодка
    print("======== Демонстрация возможностей робота летающая-лодка ============")
    flybot = FlyingBoatBot('Model#Catalina', 'USRobotics', 'SeaCat', 122, 20, aviation_engine, 200.1, 2)
    flybot.check_fuel           #
    flybot.go_to(50)            # сработка пользовательского исключения, вынесенногоо в класс LowFuelError
    flybot.fuel_supply = 2250   # добавим топлива
    flybot.check_fuel           # проверим количество топлива
    flybot.go_to(50)            # отправим робота в путь
    flybot.get_capability       # получим возможности робота, перегрузка метода get_capability 

if __name__ == '__main__':
    main()
