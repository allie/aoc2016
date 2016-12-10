import re

def parse(file_name):
	instr = ""
	cmds = []

	with open(file_name) as f:
		instr = f.read()

	instr = "".join(instr.split())

	result = ""
	i = 0
	while i < len(instr):
		c = instr[i]
		if c == "(":
			rest = instr[i:]
			close = rest.find(")")
			cmd = rest[1:close].split("x")
			dims = (int(cmd[0]), int(cmd[1]))
			i += close + 1
			chunk = instr[i:i+dims[0]]
			result += (chunk * dims[1])
			i += dims[0]
			print(dims, chunk)
		else:
			result += c
			i += 1

	return len(result)

if __name__ == "__main__":
	print(parse("input.txt"))
