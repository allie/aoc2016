def parse(file_name):
	instr = []
	x = 0
	y = 0
	facing = 0

	with open(file_name) as f:
		instr = f.readline().split(", ")

	for cmd in instr:
		turn = cmd[0]
		dist = int(cmd[1:])
		if turn == "R":
			facing = facing + 1 if facing != 3 else 0
		elif turn == "L":
			facing = facing - 1 if facing != 0 else 3
		if facing == 0: # North
			y += dist
		elif facing == 1: # East
			x += dist
		elif facing == 2: # South
			y -= dist
		elif facing == 3: # West
			x -= dist
	return abs(x) + abs(y)

if __name__ == "__main__":
	print(parse("input.txt"))
