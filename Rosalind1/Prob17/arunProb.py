def MostProb(text,k,numA,numC,numG,numT):
	retString = ""
	finalProb = 0.0
	for i in range(len(text)-k+1):
		probNucleotide = 1.0
		kMer = text[i:i+k]
		for j in range(len(kMer)):
			if kMer[j] == 'A':
				probNucleotide = probNucleotide * numA[j]
			if kMer[j] == 'C':
				probNucleotide = probNucleotide * numC[j]
			if kMer[j] == 'G':
				probNucleotide = probNucleotide * numG[j]
			if kMer[j] == 'T':
				probNucleotide = probNucleotide * numT[j]
		if probNucleotide > finalProb:
			finalProb = probNucleotide
			retString = kMer
	print retString
	return retString

f = open("input.txt", 'r')
text = f.readline().strip()
k = int(f.readline().strip())
numA = map(float,f.readline().strip().split(" "))
numC = map(float,f.readline().strip().split(" "))
numG = map(float,f.readline().strip().split(" "))
numT = map(float,f.readline().strip().split(" "))
MostProb(text,k,numA,numC,numG,numT)