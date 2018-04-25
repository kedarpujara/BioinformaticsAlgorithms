def multiLCS(string1, string2, string3)
	len1 = len(string1)
	len2 = len(string2)
	len3 = len(string3)

	dist = [[[0 for k in range(len3+1)] for j in range(len2+1)] for i in range(len1+1)]
	backtrack = [[[0 for k in range(len3+1)] for j in range(len2+1)] for i in range(len1+1)]

	for i in range(1, len1+1):
		for j in range(1, len2+1):
			for j in range(1, len3+1):
				scores = dist[i-1][j-1][k-1] + int(v)