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

NumberToPattern(5476,7);