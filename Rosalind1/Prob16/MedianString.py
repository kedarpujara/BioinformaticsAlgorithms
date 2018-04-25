import math 

def MedianString(dna,k):
	distance = 999999999999999

	for i in range(int(math.pow(4,k))):
		patternString = NumberToPattern(i,k)			
		hDist = minHamming(patternString,dna)
		if distance > hDist:
			distance = hDist
			medianstr = patternString			
	print medianstr
	return medianstr



	
def NumberToPattern(index, k):
	if k == 1:
		return NumberToSymbol(index);
	prefixIndex = index/4;
	r  = index % 4;
	symbol = NumberToSymbol(r);
	prefixPattern = NumberToPattern(prefixIndex, k-1);

	return prefixPattern + symbol;

def NumberToSymbol(letter):
	if letter == 0:
		return "A";
	if letter == 1:
		return "C";
	if letter == 2:
		return "G";
	if letter == 3:
		return "T";

def HammingDistance(dna1, dna2):
	list1 = list(dna1)
	list2 = list(dna2)
	count = 0;
	for i in range(0,len(dna1)):
		if list1[i] != list2[i]:
			count = count+1;
	return count;

def minHamming(pattern, dna):
	total = 0
	k = len(pattern)
	for string in dna:
		minH = 99999999999999
		for i in range(len(string)-k+1):
			text = string[i:k+i]
			count = HammingDistance(pattern,text)
			if count < minH:
				minH = count
		total += minH
	return total

f = open("input3.txt", 'r')
k = int(f.readline().strip())
DNA = []
for line in f:
	DNA.append(line.strip())
output = open("output.txt", 'w')
output.write(MedianString(DNA, k))
