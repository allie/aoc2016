def most_common(lst):
    return max(set(lst), key=lst.count)

def parse(file_name):
	instr = []
	with open(file_name) as f:
		instr = f.readlines()

	columns = [[],[],[],[],[],[],[],[]]
	for line in instr:
		s = line.split("\n")[0]
		if s != "":
			for i in range(len(s)):
				columns[i].append(s[i])

	result = ""
	for col in columns:
		c = most_common(col)
		result += c

	return result

if __name__ == "__main__":
	print(parse("input.txt"))
