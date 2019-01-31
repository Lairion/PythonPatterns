from lazy_init import LazyInit

if __name__ == '__main__':
	instance_one = LazyInit.get_instance();
	instance_two = LazyInit.get_instance();
	print("-"*20);
	print('Two reference point to the same instance', instance_one, instance_two,sep="\n");
