class Computer:

	@classmethod
	def builder_creations(cls,builder):
		return cls(
			builder.memory,
			builder.proccesor,
			builder.ram,
			builder.drive
			)

	def __init__(self,memory,proccesor,ram,drive):
		self.__memory = memory
		self.__proccesor = proccesor
		self.__ram = ram
		self.__drive = drive

	def get_memory(self):
		return self.__memory

	def get_processor(self):
		return self.__proccesor

	def get_ram(self):
		return self.__ram

	def get_drive(self):
		return self.__drive

