from carFactory import CarFactory

if __name__ == '__main__':
	honda = CarFactory.create_car('Honda',4,5,7)
	ford = CarFactory.create_car('Ford',4,5,7)
	print("-"*20)
	print(honda)
	print("-"*20)
	print("-"*20)
	print(ford)
	print("-"*20)