def lcsBacktrack(string1, string2):

	dist = [[0 for y in range(len(string2)+1)] for x in range(len(string1)+1)]

	backtrack = [[0 for y in range(len(string2)+1)] for x in range(len(string1)+1)]
	diagSame = False
	for i in range(len(string1)):
		dist[i][0] = 0
		backtrack[i][0] = 0
	for j in range(len(string2)):
		dist[0][j] = 0
		backtrack[0][j] = 0

	for i in range(1,len(string1)+1):
		for j in range(1,len(string2)+1):
			if string1[i] == string2[j]:
				diagSame = True
			if diagSame == True:
				dist[i][j] = max(dist[i-1][j],dist[i][j-1],dist[i-1][j-1]+1)
			else:
				dist[i][j] = max(dist[i-1][j],dist[i][j-1],dist[i-1][j-1])				
			if dist[i][j] == dist[i-1][j]:
				backtrack[i][j] = "down"
			elif dist[i][j] == dist[i][j-1]:
				backtrack[i][j] = "right"
			elif (dist[i][j] == dist[i-1][j-1] + 1) and (string1[i] == string2[j]):
				backtrack[i][j] = "diag"
			print(string1[i])
	return backtrack




def iterativeOutputLCS(backtrack, v, w):
	LCS = "" 
	i = len(v)-1
	j = len(w)-1

	while i > 0 and j > 0:
		if backtrack[i][j] == "down":
			i = i-1
		elif backtrack[i][j] == "right":
			j = j-1
		elif backtrack[i][j] == "diag" and v[i] == w[j]:
			LCS = v[i] + LCS
			i = i-1
			j = j-1
	return LCS


string1 = "AACCTTGG"
string2 = "ACACTGTGA"

string3 = "ACAG"
string4 = "CAAG"

backtracker = lcsBacktrack(string3, string4)

stringRet = iterativeOutputLCS(backtracker, string3, string4)
print stringRet