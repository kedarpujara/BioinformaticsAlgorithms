def stringGenomePath(patterns):
	returnString = patterns[0]
	for i in range(len(patterns)-1):
		string1 = patterns[i]
		string2 = patterns[i+1]
		k = len(string1)
		if string1[i+1:k-1] == string2[i:k-2]:
			returnString += string2[k-1]

	#print returnString
	return returnString



def main():
	inputFile = open("input5.txt","r")
	patterns = []
	for line in inputFile:
		patterns.append(line.strip())
	output = open("output.txt","w")
	output.write(stringGenomePath(patterns))

main()