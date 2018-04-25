def trieMatching(text, patterns):
	indices = []
	for pattern in patterns:
		for i in range(0,len(text)):
			k = len(pattern)
			if pattern == text[i:i+k]:
				indices.append(str(i))
			else:
				continue
	return indices


def main():
	inputFile = open('input2.txt')	
	patterns = []
	text = inputFile.readline().strip()
	for line in inputFile:
		patterns.append(line.strip())

	indices = trieMatching(text, patterns)
	print " ".join(indices)

main()