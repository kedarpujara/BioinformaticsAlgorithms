import math

def FreqArray(dna, k):
	freqAr = []

	for i in range(0,pow(4,k)-1):
		freqAr.append(0);
	for i in range(0, len(dna)-k):
		pattern = dna[i:k+i]
		j = PatternToNumber(pattern);
		freqAr[j] = freqAr[j] + 1;
	print freqAr;
	return freqAr;


def ComputingFreqArray(Text, k):
	freqPattern = []
	list1 = []
	freqArray = FreqArray(Text, k)
	for key,v in freqArray.items():
		freqArray[NumberToPattern(key, k)] = freqArray.pop(key)
		freqArray[NumberToPattern(key, k)] = 0
	for i in range(len(Text)-k+1):
		kpattern = Text[i:i+k]
		for key in freqArray:
			if kpattern == key:
				freqArray[key] += 1
	for key, v in sorted(freqArray.items()):
		list1.append(v)


	print " ".join(freqArray)
	return freqArray



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
	print(max(list1))
	return max(list1)


def NumberToPattern(index, k):
	if k == 1:
		return NumberToSymbol(index);

	prefixIndex = index/4;
	r  = index % 4;
	symbol = NumberToSymbol(r);
	prefixPattern = NumberToPattern(prefixIndex, k-1);

	print prefixPattern + symbol;
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

ComputingFreqArray("ACGCGGCTCTGAAA",2)
