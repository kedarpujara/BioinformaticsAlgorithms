def FreqMismatch(dna, k, d):






def freqWords(dna, k):
	global list1;
	list1 = [];
	i = 0; index = 0;
	currCount = 0;
	count = 0;
	for i in range(0,len(dna)-k):
		pattern = dna[i:(i+k-1)];
		currCount = Count(dna,pattern);
		#print currCount;
		if currCount >= count:
			count = currCount;
		maxCount = count;
		print(currCount);
	for i in range(0, len(dna)-k):
		pattern = dna[i:(i+k-1)];
		if maxCount == Count(dna, pattern):
			print pattern;
			list1.append(pattern)

	print " ".join(list1)
	return list1;

def Count(text, pattern):
	count = 0; 
	strLength = len(text) - len(pattern);

	for i in range(0,strLength):
		substr = text[i:len(pattern) + i];
		if substr == pattern:
			count = count+1;
		i = i+1;
	return count;