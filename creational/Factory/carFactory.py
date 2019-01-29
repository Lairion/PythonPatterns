from car import Car
from cars_types import CARS_TYPES

class CarFactory(Car):
    __cars = CARS_TYPES 
    @classmethod
    def create_car(cls,name,label,transmision,engine_power):
        car = cls.__cars.get(name,None)
        if car:
            return car(label,transmision,engine_power)
        