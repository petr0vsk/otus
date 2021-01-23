class LowFuelError(ValueError):
    """
    исключение, которое срабатывает если топлива не хватает до точки назначения
    """
    def __init__(self, present_value, need_value):
        self.present_value = present_value
        self.need_value = need_value

    def __str__(self):
        return f"{self.present_value} топлива не достаточно, {self.need_value} ."
