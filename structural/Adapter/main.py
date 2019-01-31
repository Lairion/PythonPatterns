from adapter import BicycleAdapter,CarAdapter
from driver import Driver

if __name__ == '__main__':
	alex = Driver(BicycleAdapter());
	alex.drive()
	peter = Driver(CarAdapter());
	peter.drive()
	jack = Driver(alex);
	peter.drive()

