import re

def get_dims(text):
	close = text.find(")")
	cmd = text[1:close].split("x")
	return (int(cmd[0]), int(cmd[1]), close + 1)

def expand(text):
	size = 0
	i = 0
	chunks = []

	if not "(" in text:
		return len(text)

	while i < len(text):
		count, repeat, skip = get_dims(text[i:])
		chunks.append(text[i:i+skip+count])
		i += skip + count

	for chunk in chunks:
		count, repeat, skip = get_dims(chunk)
		size += repeat * expand(chunk[skip:])

	return size

def parse(file_name):
	instr = ""

	with open(file_name) as f:
		instr = f.read()

	instr = "".join(instr.split())

	return expand(instr)

if __name__ == "__main__":
	print(parse("input.txt"))
