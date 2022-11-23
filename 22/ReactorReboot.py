from dataclasses import dataclass
import numpy as np
import re
from typing import Tuple

def process_row(row):
	on = row[:2] == "on"

	coords = [int(coord) for coord in re.findall(r"[\-0-9]+", row)]
	coords = [(coords[2*idx], coords[2*idx+1]) for idx in range(3)]
	return on, coords

def get_data(path):
	with open(path) as file:
		data = file.read().split("\n")

	parsed_data = map(process_row, data)

	return list(parsed_data)

@dataclass
class LightCube:
	cube: np.ndarray = np.zeros((101, 101, 101), dtype=bool)
	dim: Tuple[int] = (-50, 50)

	def execute_step(self, step):
		turn_on, coords = step
		value = 1 if turn_on else 0

		cube_coords = list()
		for coord in coords:
			if coord[1] < self.dim[0] or coord[0] > self.dim[1]:
				# Change completely outside cube range
				return
			squeezed_coord = (max(self.dim[0], coord[0]), min(self.dim[1], coord[1]))
			offset_coord = tuple([coord+50 for coord in squeezed_coord])
			cube_coords.append(offset_coord)

		x, y, z = cube_coords
		self.cube[x[0]:x[1]+1, y[0]:y[1]+1, z[0]:z[1]+1] = value

	def count(self):
		return np.sum(self.cube)

def reboot(cube, steps):
	for step in steps:
		cube.execute_step(step)

def part_one():
	reboot_steps = get_data("input.txt")
	cube = LightCube()

	reboot(cube, reboot_steps)
	print(cube.count())


# def get_overlap(first_cube, second_cube):
# 	pass

# def get_cube_size(cube):
# 	sides = [cube[2*idx+1]-cube[2*idx]+1 for idx in range(3)]
# 	return reduce(lambda x, y: x*y, sides)

# def count_lights(commands):
# 	count = 0

# 	lit_cubes = list()
# 	for command, cube in commands:
# 		if command:
# 			count += get_cube_size(cube):

def part_two():
	data = get_data("smallInput.txt")

if __name__ == '__main__':
	part_one()
	part_two()