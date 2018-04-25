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

returnPattern("ATTTGTCAAAGACTGCCAGGGGA")
