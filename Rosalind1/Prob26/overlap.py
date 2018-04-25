def deBruijn(text, k):
	dictReturn = {}
	for i in range(len(text)-k+1):
		string1 = text[i:i+k-1]
		string2 = text[i+1:i+k]
		if string1 in dictReturn:
			dictReturn[string1].append(string2)
		else:
			dictReturn[string1] = [string2]
	print dictReturn
	return dictReturn

def main():
	inputFile = open("input.txt","r")
	k = int(inputFile.readline().strip())
	inputString = inputFile.readline().strip()
	dictReturn = deBruijn(inputString, k)
	output = open("output.txt", 'w')
	for i in range(len(dictReturn)):
		#indexLen = len(dictReturn[i])
		if indexLen == 1:
			output.write(dictReturn[i] + " -> " + dictReturn[i][0] + "\n")
		else:
			output.write(dictReturn[i]) + " -> "
			for i in range(indexLen):
				 dictReturn[i][indexLen] + ", "
			output.write("\n")
main()