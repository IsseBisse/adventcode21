import pandas as pd

def parse(row):
	parts = row.split(" ")
	
	command = parts[0]
	args = tuple([int(part) if part.lstrip("-").isdigit() else part for part in parts[1:]])

	return command, args

def get_data(path):
	with open(path) as file:
		data = file.read().split("\n")

	code = list(map(parse, data))

	return code

class ALU:
	def __init__(self, code, input_=None):
		self.code = code
		self.input = input_
		
		self.register = {"w": 0, "x": 0, "y": 0, "z": 0}

	def __str__(self):
		return str(self.register)

	def __get_value(self, a):
		if isinstance(a, int):
			return a
		elif isinstance(a, str):
			return self.register[a]

	def inp(self, a):
		self.register[a] = self.input.pop(0)

	def add(self, a, b):
		self.register[a] = self.register[a] + self.__get_value(b)

	def mul(self, a, b):
		self.register[a] = self.register[a] * self.__get_value(b)

	def div(self, a, b):
		if self.__get_value(b) == 0:
			raise NotImplementedError("Cannot divide by 0!")
		self.register[a] = self.register[a] // self.__get_value(b)

	def mod(self, a, b):
		if self.register[a] < 0 or self.__get_value(b) <= 0:
			raise NotImplementedError("Invalid modulus!")
		self.register[a] = self.register[a] % self.__get_value(b)

	def eql(self, a, b):
		self.register[a] = 1 if self.register[a] == self.__get_value(b) else 0

	def run(self):
		for command, args in self.code:
			func = getattr(self, f"{command}")
			func(*args)

	def run_lines(self, start, end):
		for command, args in self.code[start:end]:
			func = getattr(self, f"{command}")
			func(*args)

def part_one():
	code = get_data("input.txt")

	# monad = int("9" * 14)
	# monad_digits = [int(char) for char in str(monad)]

	for first_digit in range(1, 10):
		for second_digit in range(1, 10):
			alu = ALU(code, [first_digit, second])
			alu.run_lines(0, 18)
		
		print(first_digit, alu)

def part_two():
	code = get_data("input.txt")

if __name__ == '__main__':
	part_one()
	# part_two()

	# NOTE: Code repeats every 18 rows with slight variations
	# NOTE: Lots of div/mod 26. Alphabet-related? 
	code = get_data("input.txt")
	row_types = list()
	for start in range(18):
		row_types.append(set(code[start::18]))

	for row in row_types:
		print(row)