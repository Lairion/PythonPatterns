from builder import ComputerBuilder
from memory import MEMORY
from proccesor import PROCCESORS
from ram import RAM
if __name__ == '__main__':
	builder = ComputerBuilder()
	computers = []
	computers.append(builder.set_memory(MEMORY[0]).set_proccesor(PROCCESORS[2]).set_ram(RAM[1]).create_computer())
	computers.append(builder.set_memory(MEMORY[1]).set_proccesor(PROCCESORS[0]).set_ram(RAM[2]).create_computer())
	computers.append(builder.set_memory(MEMORY[2]).set_proccesor(PROCCESORS[1]).set_ram(RAM[0]).create_computer())
	computers.append(builder.set_memory(MEMORY[0]).set_proccesor(PROCCESORS[0]).set_ram(RAM[0]).create_computer())
	computers.append(builder.set_memory(MEMORY[1]).set_proccesor(PROCCESORS[1]).set_ram(RAM[2]).create_computer())
	for i in range(len(computers)):
		print("-"*10,i,"-"*10)
		print(computers[i])
		print("-"*23)