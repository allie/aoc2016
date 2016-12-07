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
		for i in range(len(inc) - 2):
			chunk = inc[i:i+3]
			if chunk[0] == chunk[2] and chunk[0] != chunk[1]:
				for j in range(len(exc) - 2):
					chunk2 = exc[j:j+3]
					if chunk2[0] == chunk[1] and chunk2[2] == chunk[1] and chunk2[1] == chunk[0]:
						good = True
						break
				if good:
					break

		if good:
			valid.append(line)

	return len(valid)

if __name__ == "__main__":
	print(parse("input.txt"))
