
class Memory:
	"""docstring for Memory"""
	def __init__(self,company,size,type_memory):
		self.__company = company
		self.__size = size
		self.__type = type_memory

	def get_company(self):
		return self.__company

	def get_size(self):
		return self.__size

	def get_type(self):
		return self.__type

	def __str__(self):
		return "Memory \'{ company : %s, size: %s, type: %s}\'" % (
			self.get_company(),
			self.get_size(),
			self.get_type(),
			)

MEMORY = [
	Memory('ADATA',1000000,"SSD"),
	Memory('Hitachi',200000,"HDD"),
	Memory('Toshiba',300000,"HDD")
]


