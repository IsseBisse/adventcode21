def get_data(path):
	with open(path) as file:
		data = file.read().split("\n")

	start = data[0]
	inserts = {row.split(" -> ")[0]: row.split(" -> ")[1] for row in data[2:]}

	return start, inserts

def part_one():
	start, inserts = get_data("smallInput.txt")
	
	

def part_two():
	data = get_data("smallInput.txt")

if __name__ == '__main__':
	part_one()
	# part_two()