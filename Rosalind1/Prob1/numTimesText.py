def Count(text, pattern):
	count = 0; 
	strLength = len(text) - len(pattern);

	for i in range(0,strLength):
		substr = text[i:len(pattern) + i];
		if substr == pattern:
			count = count+1;
		i = i+1;
	print(count)
	return count;

Count("ATCTGAAGCCATGAAGCCTGAAGCCCTTTGAAGCCCTGAAGCCTGAAGCCATGTTGAAGCCAACTGAAGCCTTGAAGCCGTACAGTGAAGCCGAATGAAGCCTATGAAGCCTGAAGCCATGAAGCCGTGAAGCCATTCTGAAGCCTTGAAGCCTGCTCTGAAGCCTTTGAAGCCTGAAGCCTGAAGCCTGAAGCCTGAAGCCACTTCTGAAGCCAGATGAAGCCTGAAGCCTCCATTGAAGCCGATTGAAGCCTGAAGCCTAGTATTGAAGCCTTGAAGCCTCATCGGATTAGGGTGAAGCCTGAAGCCATGAAGCCTTTGAAGCCCTTTATAGTGAAGCCCGGTGAAGCCCTGAAGCCCCGTTGAAGCCTGAAGCCCGCTTTGAAGCCTGAAGCCTGAAGCCTGAAGCCCGGTCTGAAGCCACGATGAAGCCCCTGAAGCCAAATGAAGCCATTCGTCATGAAGCCCATGAAGCCCTGAAGCCTGAAGCCGTGAAGCCTGAAGCCATGGTGAAGCCCAACGGTTGAAGCCACATGAAGCCCTAGGTGAAGCCATGAAGCCTGAAGCCTAACCAATGGATAAGTCTGAAGCCATGAAGCCCCGGCGACATTGAAGCCTGAAGCCCTGAAGCCTTGAAGCCTGAAGCCCATGAAGCCACTCAATTGAAGCCTGAAGCCATTGAAGCCCTGAAGCCGTAGTGAAGCCCAGTGAAGCCATGAAGCCATGAAGCCGTCACTGCACTTGAAGCCCTGAAGCCCATGAGGAATGAAGCCTTGAAGCCTGAAGCCTGAAGCCACCTGAAGCCTGAAGCCCTTGCTGAAGCCCTATGAAGCCCATGAAGCCATGAAGCCGAACCCTGCTTGTCGGTTGGAACACGGGCTGAAGCCGAAATAAGCTGAAGCCTGAAGCCCTGAAGCCTGAAGCCTGAAGCCATGAAGCCGACC", "TGAAGCCTG"
)