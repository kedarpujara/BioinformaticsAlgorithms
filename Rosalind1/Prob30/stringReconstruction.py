def stringReconstruction(patterns, k):
	retString = ""
	for line in patterns:

		preString = prefix(line)#line[:k-1]
		sufString = suffix(line)#line[1:k]
		for i in range(len(patterns)):
			if preString == suffix(patterns[i]):
				retString = retString + preString
			elif sufString == prefix(patterns[i]):
				retString = sufString + retString
	print retString



def stringConstructionList(leftPat, rightPat, k):
	substr = rightPat[0]
	finalStr = leftPat[0] + rightPat[-1:]
	isFinal = True
	while isFinal == True:
		if substrr in leftPat:
			index = leftPat.index(finalStr)
			finalStr += rightPat[index][-1:]
		elif finalStr not in leftPat:



def suffix(string):
	length = len(string)
	suffix = string[1:length]
	return suffix

def prefix(string):
	length = len(string)
	prefix = string[0:length-1]
	return prefix

def main():
	inputFile = open("input.txt", "r")
	k = int(inputFile.readline().strip())
	#patterns = []
	#for line in inputFile:
		#patterns.append(line.strip())
	#stringReconstruction(patterns,k)
	patLeft = []
	patRight = []
	for line in inputFile:
		patLeft.append(line[0:len(line)-2])
		patRight.append(line[1:len(line)].strip())
	stringConstructionList(patLeft, patRight, k)
#main()

def stingPrint():
	string1 = "Hello"
	print string1[:-1]

def listString():
	a = ['A', 'B', 'C', 'D']
	b = ['D', 'E', 'F']
	index = a.index('E')
	print index

listString()


