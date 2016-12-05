import hashlib

def parse(text):
	result = ""
	n = 0
	for i in range(8):
		while True:
			m = hashlib.md5()
			m.update((text + str(n)).encode("utf-8"))
			h = m.hexdigest()
			n += 1
			if h[:5] == "00000":
				result += h[5]
				break

	return result

if __name__ == "__main__":
	print(parse("wtnhxymk"))
