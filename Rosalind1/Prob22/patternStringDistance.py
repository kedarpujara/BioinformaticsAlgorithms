def patternStringDistance(pattern, dna):
	k = len(pattern)
	distance = 0
	for text in dna: 

		hDist = 999999999999
		for i in range(len(text)-k+1):
			string = text[i:i+k]
			print(string)
			if hDist > HammingDistance(pattern,string):
				hDist = HammingDistance(pattern,string)
		distance += hDist 
	return distance


def HammingDistance(dna1, dna2):
	list1 = list(dna1)
	list2 = list(dna2)
	count = 0;
	for i in range(0,len(dna1)):
		if list1[i] != list2[i]:
			count = count+1;
	return count;


def main():
	f = open("input5.txt","r")
	pattern = f.readline().strip()
	dna = []
	dna = f.readline().split(" ")
	patternStringDistance(pattern,dna)

main()