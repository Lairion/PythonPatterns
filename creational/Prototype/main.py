from car_shop import CarShop

if __name__ == '__main__':
	shop1 = CarShop()
	shop1.load_data_from_db();
	list_car1 = shop1.get_car_list()
	list_car1.append("Lexus")

	shop2 = shop1.clone()
	list_car2 = shop2.get_car_list()
	list_car2.append("Dodge")
	print("-"*5,"List car 1","-"*5)
	print(*list_car1,sep="\n") 
	print("-"*5,"List car 2","-"*5)
	print(*list_car2,sep="\n") 

	shop3 = CarShop()
	list_car3 = shop3.get_car_list()
	list_car3.append("Lexus")

	shop4 = shop3.clone()
	list_car4 = shop4.get_car_list()
	list_car4.append("Dodge")
	print("-"*5,"List car 3","-"*5)
	print(*list_car3,sep="\n") 
	print("-"*5,"List car 4","-"*5)
	print(*list_car4,sep="\n") 
