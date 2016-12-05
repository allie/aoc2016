import hashlib

def parse(text):
	result = list("________")
	n = 0
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	while "_" in result:
		m = hashlib.md5()
		m.update((text + str(n)).encode("utf-8"))
		h = m.hexdigest()
		n += 1
		if h[:5] == "00000":
			x = h[5]
			if x not in alphabet and int(x) < 8 and result[int(x)] == "_":
				result[int(x)] = h[6]

	return "".join(result)

if __name__ == "__main__":
	print(parse("wtnhxymk"))
