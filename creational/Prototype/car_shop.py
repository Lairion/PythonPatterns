import copy

class CarShop:
	"""docstring for CarShop"""

	def __init__(self):
		self.__car_list = [] 

	def load_data_from_db(self):
		self.__car_list.append("Honda")
		self.__car_list.append("Ford")
		self.__car_list.append("Mersedes")

	def get_car_list(self):
		return self.__car_list

	def clone(self):
		return copy.copy(self)
	
