class Ram:
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
		return "Ram \'{ company : %s, size: %s, type: %s}\'" % (
			self.get_company(),
			self.get_size(),
			self.get_type(),
			)

RAM = [
	Ram('Kingstone',1000,"DDR2"),
	Ram('Samsung',2000,"DDR4"),
	Ram('HiperX',3000,"DDR3")
]