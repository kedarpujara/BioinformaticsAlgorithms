def deBruijnCollection(Patterns):
	dictReturn = {}
	for line in Patterns:
		k = len(line)
		string1 = line[:-1]
		string2 = line[1:]
		if string1 in dictReturn:
			dictReturn[string1].append(string2)
		else:
			dictReturn[string1] = [string2]
	#print dictReturn
	return dictReturn



def main():
	inputFile = open("input2.txt","r")
	patterns = []
	for line in inputFile:
		patterns.append(line.strip())
	dictReturn = deBruijnCollection(patterns)
	output = open("output.txt","w")
	#print(dictReturn)
	for value in dictReturn:
		output.write(value + " -> ")
		for i in range(len(dictReturn[value])):
			if i > 0:
				output.write(",")
				output.write(dictReturn[value][i])
			else:
				output.write(dictReturn[value][i])
		output.write("\n")

main()
