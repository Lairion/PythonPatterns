from van import Van
class Driver(Van):
	"""docstring for Driver"""
	def __init__(self,van):
		print(type(van))
		self.__van = van
		print(type(self.__van))

	def drive(self):
		print(type(self.__van))
		print(type(self))
		if isinstance(self.__van,type(self)):
			print("Riding a driver")
			return
		self._van.drive()
		