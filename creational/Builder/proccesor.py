
class Proccesor:
	"""docstring for Memory"""
	def __init__(self,family,frequence,socket_processor):
		self.__family = family
		self.__frequence = frequence
		self.__socket = socket_processor

	def get_family(self):
		return self.__family

	def get_frequence(self):
		return self.__frequence

	def get_socket(self):
		return self.__socket

	def __str__(self):
		return "Proccesor \'{ company : %s, frequence: %s, socket: %s}\'" % (
			self.get_family(),
			str(self.get_frequence()),
			self.get_socket()
			)

PROCCESORS = [
	Proccesor('AMD A-Series',1500,"AM3+"),
	Proccesor('Intel Core i3',2500,"1150"),
	Proccesor('Intel Core i7',3500,"1151")
]