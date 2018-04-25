def deBruijn(text, k):
	dictReturn = {}
	for i in range(len(text)-k+1):
		string1 = text[i:i+k-1]
		string2 = text[i+1:i+k]
		print(string1)
		if string1 in dictReturn:
			dictReturn[string1] += ", " + string2
		else:
			dictReturn[string1] = string2
	print dictReturn
	return dictReturn

def main():
	inputFile = open("input5.txt","r")
	k = int(inputFile.readline().strip())
	inputString = inputFile.readline().strip()
	dictReturn = deBruijn(inputString, k)
	output = open("output.txt", 'w')
	for i in dictReturn:
		output.write(i + " -> " + dictReturn[i] + "\n")



main()