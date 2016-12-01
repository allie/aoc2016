def parse(file_name):
	instr = []
	history = []
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
			while dist > 0:
				y += 1
				pos = (x, y)
				if pos in history:
					break
				history.append(pos)
				dist -= 1
			if dist > 0:
				break
		elif facing == 1: # East
			while dist > 0:
				x += 1
				pos = (x, y)
				if pos in history:
					break
				history.append(pos)
				dist -= 1
			if dist > 0:
				break
		elif facing == 2: # South
			while dist > 0:
				y -= 1
				pos = (x, y)
				if pos in history:
					break
				history.append(pos)
				dist -= 1
			if dist > 0:
				break
		elif facing == 3: # West
			while dist > 0:
				x -= 1
				pos = (x, y)
				if pos in history:
					break
				history.append(pos)
				dist -= 1
			if dist > 0:
				break

	return abs(x) + abs(y)

if __name__ == "__main__":
	print(parse("input.txt"))
