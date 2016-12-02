def parse(file_name, keypad, start_x, start_y):
	instr = []
	code = []
	x = start_x
	y = start_y

	with open(file_name) as f:
		instr = f.readlines()

	for line in instr:
		for i in line:
			if i == "U":
				y = y - 1 if y > 0 and keypad[y - 1][x] != -1 else y
			elif i == "D":
				y = y + 1 if y < len(keypad) - 1 and keypad[y + 1][x] != -1 else y
			elif i == "L":
				x = x - 1 if x > 0 and keypad[y][x - 1] != -1 else x
			elif i == "R":
				x = x + 1 if x < len(keypad[y]) - 1 and keypad[y][x + 1] != -1 else x
		code.append(keypad[y][x])

	return code

if __name__ == "__main__":
	print("Part 1: ", parse("input.txt", [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
	print("Part 2: ", parse("input.txt", [[-1, -1, 1, -1, -1], [-1, 2, 3, 4, -1], [5, 6, 7, 8, 9], [-1, "A", "B", "C", -1], [-1, -1, "D", -1, -1]], 0, 2))
