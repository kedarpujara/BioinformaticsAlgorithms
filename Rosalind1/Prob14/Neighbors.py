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
	return neighborhood;

def HammingDistance(dna1, dna2):
	list1 = list(dna1)
	list2 = list(dna2)
	count = 0;
	for i in range(0,len(dna1)):
		if list1[i] != list2[i]:
			count = count+1;

	return count;
