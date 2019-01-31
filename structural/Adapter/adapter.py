from bicycle import Bicycle
from car import Car
from van import Van
class BicycleAdapter(Van):
	"""docstring for BicycleAdapter"""
	def __init__(self):
		self.__bicycle = Bicycle()
		
	def drive(self):
		self.__bicycle.ride()

class CarAdapter(Van):
	def __init__(self):
		self.__car = Car()
		
	def drive(self):
		self.__car.ride()

