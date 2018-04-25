from random import randint
import math 

def RandomMotifSearches(dna, k, t):
	motifs = []
	bestMotifs = []

	for string in dna:
		i = randint(0,len(string)-k)
		kmer = string[i:i+k]
		bestMotifs.append(kmer)
	motifs = bestMotifs
	while True:
		numA,numC,numG,numT = Profile(k, t, bestMotifs)
		motifs = []
		for strand in dna: 
			motifs.append(MostProb(strand,k,numA,numC,numG,numT))
			if Score(motifs) < Score(bestMotifs):
				bestMotifs = motifs
			else:
				return bestMotifs

def RandomMotifSearch(DNA, k, t):
    bestMotifs = []
    for string in DNA:
        i = randint(0, len(string) - k)
        kmer = string[i:i+k]
        bestMotifs.append(kmer)
    motifs = bestMotifs
    while True:
        numA,numC,numG,numT = Profile(k,t,motifs)
        motifs = []
        for string in DNA:
            motifs.append(MostProb(string,k,numA,numC,numG,numT))
        if Score(motifs) < Score(bestMotifs):
            bestMotifs = motifs
        else:
            return bestMotifs, Score(bestMotifs)


def Consensus(motifs):
	k = len(motifs[0])
	numA = [0]*k
	numC = [0]*k
	numG = [0]*k
	numT = [0]*k
	for kMer in motifs:
		for i in range(len(kMer)):
			if kMer == 'A':
				numA[i] += 1
			if kMer == 'C':
				numC[i] += 1
			if kMer == 'G':
				numG[i] += 1
			if kMer == 'T':
				numT[i] += 1		
	consensusSeq = ""
	for i in range(k):
		maxProbLetter = max(numA[i], numC[i], numG[i], numT[i])
		if numA[i] == maxProbLetter:
			consensusSeq += 'A'
		elif numC[i] == maxProbLetter:
			consensusSeq += 'C'
		elif numG[i] == maxProbLetter:
			consensusSeq += 'G'
		elif numT[i] == maxProbLetter:
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

def Profile(k,t,strings):
	numA = [1.0]*k
	numC = [1.0]*k
	numG = [1.0]*k
	numT = [1.0]*k
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


def SymbolToNumber(letter):
	if letter == "A":
		return 0;
	if letter == "C":
		return 1;
	if letter == "G":
		return 2;
	if letter == "T":
		return 3;

def NumberToSymbol(letter):
	if letter == 0:
		return "A";
	if letter == 1:
		return "C";
	if letter == 2:
		return "G";
	if letter == 3:
		return "T";

def NumberToPattern(index, k):
	if k == 1:
		return NumberToSymbol(index);

	prefixIndex = index/4;
	r  = index % 4;
	symbol = NumberToSymbol(r);
	prefixPattern = NumberToPattern(prefixIndex, k-1);

	print prefixPattern + symbol;
	return prefixPattern + symbol;


def PatternToNumber(pattern):
	if len(pattern) == 0:
		return 0;

	return 4*PatternToNumber(pattern[:-1]) + SymbolToNumber(pattern[-1])

f= open("input.txt", "r")
k = int(f.readline().strip())
t = int(f.readline().strip())
dna = []
for line in f:
	dna.append(line.strip())
topScore = 9999999999
motifs = []
for i in range(1000):
	retAnswer, score = RandomMotifSearches(dna,k,t)
	if score < topScore:
		topScore = score
		motifs = retAnswer

output = open("output.txt","w")
for motif in motifs:
	output.write(motif + "\n")









