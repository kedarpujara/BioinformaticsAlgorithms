def MotifEnumeration(dna, k, d):
	patterns = []
	for strand in dna:
		for i in range(len(strand)-k+1):
			string = strand[i:i+k]
			nieghborPattern = Neighbors(string,d)			
			for item in nieghborPattern:
				for strand2 in dna:
					appearsInAll = False
					for j in range(len(strand2)-k+1):
						string2 = strand2[j:j+k]
						nieghborPattern2 = Neighbors(string2,d)
						if item in nieghborPattern2:
							appearsInAll = True
							break
					if appearsInAll == False:
						break
				if appearsInAll:
					patterns.append(item)
	patterns = list(set(patterns))
	print " ".join(patterns)
	return sorted(patterns)




def HammingDistance(dna1, dna2):
	list1 = list(dna1)
	list2 = list(dna2)
	count = 0;
	for i in range(0,len(dna1)):
		if list1[i] != list2[i]:
			count = count+1;
	return count;


def Neighbors(pattern, d):
	if d == 0:
		return [pattern];
	if len(pattern) == 1:
		return ['A','C','G','T'];
	neighborhood = [];
	suffixNeighbors = Neighbors(pattern[1:], d);
	for i in suffixNeighbors:
		if HammingDistance(pattern[1:],i) < d:
			for x in ['A','C','G','T']:
				neighborhood.append(x+i)
		else:
			neighborhood.append(pattern[0]+i)
	return neighborhood

f = open("input.txt", 'r')
k,d = map(int, f.readline().split(" "))
DNA = []
for line in f:
  DNA.append(line.strip())
MotifEnumeration(DNA, k, d)