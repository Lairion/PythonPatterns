class LazyInit:
	"""docstring for LazyInit"""
	_instance = None
	@classmethod
	def get_instance(cls):
		if cls._instance == None:
			cls._instance = LazyInit()
		return cls._instance
		