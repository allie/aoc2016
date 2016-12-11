def parse(file_name):
	instr = []
	robots = []
	outputs = []

	for i in range(300):
		robots.append([])
		outputs.append([])

	with open(file_name) as f:
		instr = f.readlines()

	queued = instr

	while len(queued) > 0:
		for line in instr:
			s = line.split(" ")
			if line[0] == "v": # value X goes to bot Y
				robots[int(s[-1])].append(int(s[1]))
				queued.remove(line)
			else: # bot X gives low to [bot/output] Y and high to [bot/output] Z
				i = int(s[1])
				assert len(robots[i]) <= 2, "Robots can't carry that much"
				if len(robots[i]) < 2:
					continue
				low = min(robots[i])
				high = max(robots[i])
				recipient_low = int(s[6])
				recipient_high = int(s[-1])
				if s[5] == "output":
					outputs[recipient_low].append(low)
				else:
					robots[recipient_low].append(low)
				if s[-2] == "output":
					outputs[recipient_high].append(high)
				else:
					robots[recipient_high].append(high)
				robots[i].remove(low)
				robots[i].remove(high)
				queued.remove(line)
			# Check robots for values 61 and 17
			for i in range(len(robots)):
				if robots[i] == [61, 17]:
					return "Robot " + str(i) + " has 61 and 17!"
		instr = queued

	for i in range(len(robots)):
		if len(robots[i]) > 0:
			print("robot", i, robots[i])

	for i in range(len(outputs)):
		if len(outputs[i]) > 0:
			print("output", i, outputs[i])

if __name__ == "__main__":
	print(parse("input.txt"))
