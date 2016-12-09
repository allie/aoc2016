lcd = []

def rect(width, height):
	for i in range(height):
		for j in range(width):
			lcd[i][j] = 1
	print(lcd)

def rrow(row, amount):
	right = lcd[row][-amount:]
	left = lcd[row][:-amount]
	right.extend(left)
	lcd[row] = right
	print(lcd)

def rcol(col, amount):
	top = []
	bottom = []
	for i in range(len(lcd)):
		if i < (len(lcd) - amount):
			top.append(lcd[i][col])
		else:
			bottom.append(lcd[i][col])
	print(top, bottom)
	bottom.extend(top)
	for i in range(len(lcd)):
		lcd[i][col] = bottom[i]
	print(lcd)

def count():
	c = 0
	for i in range(len(lcd)):
		for j in range(len(lcd[i])):
			c += lcd[i][j]
	return c

def parse(file_name):
	instr = []

	for i in range(6):
		lcd.append([])
		for j in range(50):
			lcd[i].append(0)

	with open(file_name) as f:
		instr = f.readlines()

	for line in instr:
		line = line.replace("\n", "")
		if "rect" in line:
			dims = line.split(" ")[1].split("x")
			print("rect", dims[0], dims[1])
			rect(int(dims[0]), int(dims[1]))
		elif "x=" in line:
			dims = line.split("x=")[1].split(" by ")
			print("rcol", dims[0], dims[1])
			rcol(int(dims[0]), int(dims[1]))
		elif "y=" in line:
			dims = line.split("y=")[1].split(" by ")
			print("rrow", dims[0], dims[1])
			rrow(int(dims[0]), int(dims[1]))

	return count()

if __name__ == "__main__":
	print(parse("input.txt"))
