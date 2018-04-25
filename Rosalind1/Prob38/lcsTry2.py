def LCS(str1, str2):
	len1 = len(str1)
	len2 = len(str2)
	c = [[0 for y in range(len2)] for x in range(len1)]
	b = [[0 for y in range(len2)] for x in range(len1)]

	for i in range(1,len1):
		c[i][0] = 0

	for j in range(1,len2):
		c[0][j] = 0

	for i in range(1,len1):
		for j in range(1,len2):
			if(str1[i] == str2[j]):
				c[i][j] = c[i-1][j-1]
				b[i][j] = c[i-1][j-1]
			elif c[i-1][j] >= c[i][j-1]:
				c[i][j] = c[i-1][j]
				b[i][j] = b[i-1][j]
			else:
				c[i][j] = c[i][j-1]
				b[i][j] = b[i][j-1]
	print c
	return c



string1 = "AACCTTGG"
string2 = "ACACTGTGA"
string3 = "AAA"
string4 = "AAAA"
LCS(string3,string4)
