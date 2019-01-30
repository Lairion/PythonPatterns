from computer import Computer

class ComputerBuilder(object):
	__memory = ""
	__proccesor = ""
	__ram = ""

	def set_memory(self,memory):
		self.__memory = memory
		return self

	def set_proccesor(self,proccesor):
		self.__proccesor = proccesor
		return self

	def set_ram(self,ram):
		self.__ram = ram
		return self

	def get_parameters(self):
		return {
			'memory':self.__memory,
			'proccesor':self.__proccesor,
			'ram':self.__ram,
		}

	def create_computer(self):
		return Computer(**self.get_parameters())
		