def parse(file_name):
	instr = []
	tmp = []
	tris = []
	valid = []

	with open(file_name) as f:
		instr = f.readlines()

	for line in instr:
		tmp.append([int(s) for s in line.split() if s.isdigit()])

	current = []
	for i in range(3):
		for tri in tmp:
			current.append(tri[i])
			if len(current) == 3:
				tris.append(current)
				current = []

	for tri in tris:
		if tri[0] + tri[1] > tri[2] and tri[0] + tri[2] > tri[1] and tri[1] + tri[2] > tri[0]:
			valid.append(tri)

	return len(valid)

if __name__ == "__main__":
	print(parse("input.txt"))
