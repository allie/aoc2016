def most_common(lst):
	return max(set(lst), key=lst.count)

def parse(file_name):
	instr = []
	valid = []

	with open(file_name) as f:
		instr = f.readlines()[:-1]

	for line in instr:
		letters = "".join(line.split("-")[:-1])
		tmp = line.split("[")
		result = tmp[1].split("]")[0]
		num = int(tmp[0].split("-").pop().split()[0]
		d = {}
		for char in letters:
			d[char]=d.get(char,0)+1
		ordered = sorted(d.items(), key=lambda x: (x[0], x[1]))
		ordered.sort(key=lambda x: x[1], reverse=True)
		print(ordered)
		val = "".join([x[0] for x in ordered])[:5]
		if (val == result):
			valid.append(num)

	return(sum(valid))


if __name__ == "__main__":
	print(parse("input.txt"))
