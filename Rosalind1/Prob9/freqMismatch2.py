def FrequentWordsMismatches(Text, k, d):
	freqPatterns = [];
	close = []
	freqAr = []
	for i in range(0,pow(4,k)-1):
		close.append(0);
		freqAr.append(0);

	for i in range(0, len(Text)-k):
		neighborhood = Neighbors(Text[i:k+i],d)
		for pat in neighborhood:
			index = PatternToNumber(pat);
			close[index] = 1;
	for i in range(0,pow(4,k)-1):
		if close[i] == 1:
			pattern = NumberToPattern(i,k);
			freqAr[i] = approximatePatternCount(Text, pattern, d);

	maxCount = max(freqAr);

	for i in range(pow(4,k)-1):
		if freqAr[i] == maxCount:
			pattern = NumberToPattern(i,k);
			freqPatterns.append(pattern);

	print " ".join(freqPatterns);
	return freqPatterns;


def approximatePatternCount(text, pattern, d):
	count = 0
	for i in range(len(text) - len(pattern) + 1):
		compPattern = text[i:i+len(pattern)]
		if HammingDistance(pattern, compPattern) <= d:
			count +=1
	return count




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


def PatternToNumber(pattern):
	if len(pattern) == 0:
		return 0;

	return 4*PatternToNumber(pattern[:-1]) + SymbolToNumber(pattern[-1])

def SymbolToNumber(letter):
	if letter == "A":
		return 0;
	if letter == "C":
		return 1;
	if letter == "G":
		return 2;
	if letter == "T":
		return 3;

def returnPattern(pattern):
	list1 = []
	list1.append(PatternToNumber(pattern))
	
	#print(max(list1))
	return max(list1)

def NumberToPattern(index, k):
	if k == 1:
		return NumberToSymbol(index);

	prefixIndex = index/4;
	r  = index % 4;
	symbol = NumberToSymbol(r);
	prefixPattern = NumberToPattern(prefixIndex, k-1);

	#print prefixPattern + symbol;
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

FrequentWordsMismatches("CCGCATCACTACCTACGGCCACACCAATAACAAACCGCATCACGCCACACCAATAACAAACCGCATCACTACCTACGGCCACACCAATAACAAAGCCACACCGCCACACCAATAACAAAGCCACACCGAGCGTGATGTACCTACGTACCTACGCCGCATCACCCGCATCACTACCTACGGCCACACCAATAACAAATACCTACGTACCTACGGCCACACCTACCTACGAATAACAAATACCTACGGAGCGTGATGGCCACACCGCCACACCTACCTACGGCCACACCAATAACAAACCGCATCACTACCTACGAATAACAAAGAGCGTGATGAATAACAAACCGCATCACAATAACAAAAATAACAAATACCTACGGAGCGTGATGTACCTACGTACCTACGGCCACACCTACCTACGCCGCATCACGCCACACCGAGCGTGATGGAGCGTGATGAATAACAAAGCCACACCAATAACAAAGAGCGTGATGCCGCATCACGAGCGTGATGGAGCGTGATGAATAACAAAAATAACAAACCGCATCACTACCTACGTACCTACGCCGCATCACAATAACAAAGCCACACCGAGCGTGATGGAGCGTGATGAATAACAAAGCCACACCCCGCATCACTACCTACGTACCTACGGCCACACCGAGCGTGATGCCGCATCACGCCACACCGAGCGTGATGCCGCATCACAATAACAAAAATAACAAAAATAACAAAGAGCGTGATGTACCTACGTACCTACGAATAACAAAAATAACAAAAATAACAAATACCTACGAATAACAAAGAGCGTGATGCCGCATCACGCCACACCTACCTACGAATAACAAAAATAACAAAGAGCGTGATGCCGCATCACAATAACAAAGCCACACCGAGCGTGATGTACCTACGCCGCATCACCCGCATCAC",6,2)
