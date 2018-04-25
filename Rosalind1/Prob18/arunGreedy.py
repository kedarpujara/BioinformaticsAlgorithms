def Consensus(Motifs):
	k = len(Motifs[0])
	Acount = [0]*k
	Ccount = [0]*k
	Gcount = [0]*k
	Tcount = [0]*k
	for kmer in Motifs:
		for i in range(len(kmer)):
			if kmer[i] == 'A':
				Acount[i] += 1
			if kmer[i] == 'C':
				Ccount[i] += 1
			if kmer[i] == 'G':
				Gcount[i] += 1
			if kmer[i] == 'T':
				Tcount[i] += 1
	cmotif = ""
	for i in range(k):
		m = max(Acount[i], Ccount[i], Gcount[i], Tcount[i])
		if Acount[i] == m:
			cmotif += 'A'
		elif Ccount[i] == m:
			cmotif += 'C'
		elif Gcount[i] == m:
			cmotif += 'G'
		elif Tcount[i] == m:
			cmotif += 'T'
	return cmotif

def HammingDistance(Pattern, Text):
  count = 0
  for i in range(len(Pattern)):
    if Pattern[i] != Text[i]:
      count += 1
  return count

def Score(Motifs):
	cMotif = Consensus(Motifs)
	score = 0
	for motif in Motifs:
		score += HammingDistance(motif, cMotif)
	return score

def mostProbable(Text,k,Aprob,Cprob,Gprob,Tprob):
	mostp = ""
	prob = 0.0
	for i in range(len(Text)-k+1):
		currp = 1.0
		kmer = Text[i:i+k]
		for j in range(len(kmer)):
			if kmer[j] == 'A':
				currp = currp * Aprob[j]
			if kmer[j] == 'C':
				currp = currp * Cprob[j]
			if kmer[j] == 'G':
				currp = currp * Gprob[j]
			if kmer[j] == 'T':
				currp = currp * Tprob[j]
		if currp > prob or mostp == "":
			prob = currp
			mostp = kmer
	return mostp

def ProfileConstruction(k,t,strings):
	Acount = [0.0]*k
	Ccount = [0.0]*k
	Gcount = [0.0]*k
	Tcount = [0.0]*k
	for kmer in strings:
		for i in range(len(kmer)):
			if kmer[i] == 'A':
				Acount[i] += 1.0
			if kmer[i] == 'C':
				Ccount[i] += 1.0
			if kmer[i] == 'G':
				Gcount[i] += 1.0
			if kmer[i] == 'T':
				Tcount[i] += 1.0
	Abest = [Acount[i]/(Acount[i] + Ccount[i] + Gcount[i] + Tcount[i]) for i in range(k)]
	Cbest = [Ccount[i]/(Acount[i] + Ccount[i] + Gcount[i] + Tcount[i]) for i in range(k)]
	Gbest = [Gcount[i]/(Acount[i] + Ccount[i] + Gcount[i] + Tcount[i]) for i in range(k)]
	Tbest = [Tcount[i]/(Acount[i] + Ccount[i] + Gcount[i] + Tcount[i]) for i in range(k)]
	return Abest, Cbest, Gbest, Tbest

def GreedyMotifSearch(k,t,DNA):
	bestMotifs = []
	for string in DNA:
		bestMotifs.append(string[0:k])
	first = DNA[0]
	for i in range(len(first)-k+1):
		motifs = []
		motif = first[i:i+k]
		motifs.append(motif)
		for j in range(1, t):
			Aprob, Cprob, Gprob, Tprob = ProfileConstruction(k,t,motifs)
			motifs.append(mostProbable(DNA[j],k,Aprob,Cprob,Gprob,Tprob))
		if Score(motifs) < Score(bestMotifs):
			bestMotifs = motifs
	return bestMotifs

f = open("input.txt", 'r')
k, t =  map(int,f.readline().strip().split(" "))
DNA = []
for line in f:
	DNA.append(line.strip())
output = open("output.txt", 'w')
answer = GreedyMotifSearch(k,t,DNA)
for i in answer:
	output.write(i + '\n')