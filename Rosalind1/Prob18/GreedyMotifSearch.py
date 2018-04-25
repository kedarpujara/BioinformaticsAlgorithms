def Consensus(motifs):
	k = len(motifs[0])
	numA = [0]*k
	numC = [0]*k
	numG = [0]*k
	numT = [0]*k
	for kMer in motifs:
		for i in range(len(kMer)):
			if kMer[i] == 'A':
				numA[i] += 1
			if kMer[i] == 'C':
				numC[i] += 1
			if kMer[i] == 'G':
				numG[i] += 1
			if kMer[i] == 'T':
				numT[i] += 1		
	consensusSeq = ""
	for j in range(k):
		maxProbLetter = max(numA[j], numC[j], numG[j], numT[j])
		if numA[j] == maxProbLetter:
			consensusSeq += 'A'
		elif numC[j] == maxProbLetter:
			consensusSeq += 'C'
		elif numG[j] == maxProbLetter:
			consensusSeq += 'G'
		elif numT[j] == maxProbLetter:
			consensusSeq += 'T'
	return consensusSeq

def HammingDistance(dna1, dna2):
	list1 = list(dna1)
	list2 = list(dna2)
	count = 0;
	for i in range(0,len(dna1)):
		if list1[i] != list2[i]:
			count = count+1;
	return count;

def Score(motifs):
	consensusSeq = Consensus(motifs)
	score = 0
	for motif in motifs:
		hDist = HammingDistance(motif,consensusSeq)
		score += hDist
	return score


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
    if probNucleotide > finalProb or retString == "":
      finalProb = probNucleotide
      retString = kMer  
  return retString

def Profile(k,t,strings):
	numA = [0.0]*k
	numC = [0.0]*k
	numG = [0.0]*k
	numT = [0.0]*k
	for kMer in strings:
		for i in range(len(kMer)):
			if kMer[i] == 'A':
				numA[i] += 1.0
			if kMer[i] == 'C':
				numC[i] += 1.0
			if kMer[i] == 'G':
				numG[i] += 1.0
			if kMer[i] == 'T':
				numT[i] += 1.0	
	maxA = [numA[i]/(numA[i] + numC[i] + numG[i] + numT[i]) for i in range(k)]
	maxC = [numC[i]/(numA[i] + numC[i] + numG[i] + numT[i]) for i in range(k)]
	maxG = [numG[i]/(numA[i] + numC[i] + numG[i] + numT[i]) for i in range(k)]
	maxT = [numT[i]/(numA[i] + numC[i] + numG[i] + numT[i]) for i in range(k)]
	return maxA,maxC,maxG,maxT 

def GreedyMotif(k,t,dna):
	bestMotifs = []
	for string in dna:
		bestMotifs.append(string[0:k])
	string1 = dna[0]
	for i in range(len(string1)-k+1):
		motifs = []
		motif = string1[i:k+i]
		motifs.append(motif)
		for j in range(1,t):			
			numA,numC,numG,numT = Profile(k,t,motifs)
			motifs.append(MostProb(dna[j],k,numA,numC,numG,numT))
		if Score(motifs) < Score(bestMotifs):
			bestMotifs = motifs
	return bestMotifs


def main():
	f = open("input5.txt","r")
	k = int(f.readline().strip())
	t = int(f.readline().strip())
	dna = []
	for line in f:
		dna.append(line.strip())
	output = open("output.txt","w")
	searchOutput = GreedyMotif(k,t,dna)
	for i in searchOutput:
		output.write(i+"\n")


main()







