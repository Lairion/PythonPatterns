class Computer:

	@classmethod
	def builder_creations(cls,builder):
		return cls(
			builder.memory,
			builder.proccesor,
			builder.ram,
			builder.drive
			)

	def __init__(self,memory,proccesor,ram):
		self.__memory = memory
		self.__proccesor = proccesor
		self.__ram = ram
		

	def get_memory(self):
		return self.__memory

	def get_processor(self):
		return self.__proccesor

	def get_ram(self):
		return self.__ram

	

	def __str__(self):
		string = ("\n"+"-"*5+"\n")
		return "Computer \'{ \n%s \n}\'" % (string.join([
			str(self.get_memory()),
			str(self.get_ram()),
			str(self.get_processor())
			]))

