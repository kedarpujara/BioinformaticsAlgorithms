def gapGenomeString(patternLeft, patternRight, k, d):
	leftString = patternLeft[0]
	rightString = patternRight[0]
	for i in range(1,len(patternLeft)):
		leftString += suffix(patternLeft[i])
	for i in range(1,len(patternRight)):
		rightString += suffix(patternRight[i])
	finalString = leftString[:k+d] + rightString

	#finalString += patternRight[0][d:]
	#for i in range(1,len(patternRight)):
		#finalString += suffix(patternRight[i])
	
	return finalString


def suffix(string):
	return string[len(string)-1]


def main():
	inputFile = open("input4.txt", 'r')
	k = int(inputFile.readline().strip())
	d = int(inputFile.readline().strip())
	patternLeft = []
	patternRight = []
	for line in inputFile:
		line = line.rstrip("\n")
		stringArr = line.split('|')
		patternLeft.append(stringArr[0])
		patternRight.append(stringArr[1])
	
	outputFile = open("output.txt",'w')
	outputFile.write(gapGenomeString(patternLeft,patternRight,k,d))


main()

