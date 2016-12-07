import re

def parse(file_name):
	instr = []
	valid = []

	with open(file_name) as f:
		instr = f.readlines()

	for line in instr:
		inc = re.sub(r"\[.*?\]", "|", line)
		exc = "|".join(re.findall(r"\[(.*?)\]", line))
		good = False
		for i in range(len(inc) - 3):
			chunk = inc[i:i+4]
			if (chunk[0], chunk[1]) == (chunk[3], chunk[2]) and chunk[0] != chunk[1]:
				good = True
				break
		for i in range(len(exc) - 3):
			chunk = exc[i:i+4]
			if (chunk[0], chunk[1]) == (chunk[3], chunk[2]) and chunk[0] != chunk[1]:
				good = False
				break
		if good:
			valid.append(line)

	return len(valid)

if __name__ == "__main__":
	print(parse("input.txt"))
