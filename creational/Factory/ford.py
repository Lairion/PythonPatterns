from car import Car

class Ford(Car):
    
    def __init__(self,label,transmision,engine_power):
        self.__label = label
        self.__transmision = transmision
        self.__engine_power = engine_power

    def get_label(self):
        return self.__label

    def get_transmision(self):
        return self.__transmision

    def get_engine_power(self):
        return self.__engine_power
