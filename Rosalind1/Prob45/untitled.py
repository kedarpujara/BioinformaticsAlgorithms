def affineGapPenalty(v, w, sigma, epsilon):

	len1 = len(v)
	len2 = len(w)

	dist = [[[0 for j in xrange(len2+1)] for i in xrange(len1+1)] for k in xrange(3)]
	backtrack = [[[0 for j in xrange(len2+1)] for i in xrange(len1+1)] for k in xrange(3)]

	for i in range(1,len1+1):
		dist[0][i][0] = -sigma - (i-1)*epsilon
        dist[1][i][0] = -sigma - (i-1)*epsilon
        dist[2][i][0] = -10*sigma

	for j in range(1,len2+1):
		dist[2][0][j] = -sigma - (j-1)*epsilon
        dist[1][0][j] = -sigma - (j-1)*epsilon
        dist[0][0][j] = -10*sigma               


	for i in range(1, len1 + 1):
		for j in range(1, len2 + 1):
			lowerMatrix = [dist[0][i-1][j] - epsilon, dist[1][i-1][j] - sigma]
    		dist[0][i][j] = max(lowerMatrix)
    		backtrack[0][i][j] = lowerMatrix.index(dist[0][i][j])	
    		
    		upperMatrix = [dist[2][i][j-1] - epsilon, dist[1][i][j-1] - sigma]
    		dist[2][i][j] = max(upperMatrix)
    		backtrack[2][i][j] = upperMatrix.index(dist[2][i][j])


    		index1 = index[v[i-1]]
    		index2 = index[w[j-1]]
    		middleMatrix = [dist[0][i][j], dist[1][i-1][j-1] + scoringMatrix[index1][index2], dist[2][i][j]]
    		dist[1][i][j] = max(middleMatrix)
    		backtrack[1][i][j] = middleMatrix.index(dist[1][i][j])

	i = len1
	j = len2
	vUpdate = v
	wUpdate = w

	scores = [dist[0][i][j], dist[1][i][j], dist[2][i][j]]
	maxScore = max(scores)
	backtrackUpdate = scores.index(maxScore)

	indels = lambda word, i: word[:i] + '-' + word[i:]

	while i*j != 0:
		if backtrackUpdate == 0:
			if backtrack[0][i][j] == 1:
				backtrackUpdate = 1
			i = i-1
			wUpdate = indels(wUpdate, j)

		elif backtrackUpdate == 1:
			if backtrack[1][i][j] == 0:
				backtrackUpdate = 0
    		elif backtrackUpdate[1][i][j] == 2:
    			backtrackUpdate = 2
    		else:
    			i = i-1
    			j = j-1
    	else:
    		if backtrack[2][i][j] == 1:
    			backtrackUpdate = 1
    		j = j-1
    		vUpdate = indels(vUpdate, i)

	for _ in range(i):
		wUpdate = indels(wUpdate,0)

	for _ in range(j):
		vUpdate = indels(vUpdate,0)

	return str(maxScore), vUpdate, wUpdate



# def scoringMatrix():
# 	lines = open('scoringMatrix.txt').read().splitlines()
# 	index = {letter: ind for ind, letter in enumerate(lines[0].split())}
# 	PAM = list(map(lambda x: list(map(int, x.split()[1:])), lines[1:]))
# 	return PAM


lines = open('scoringMatrix.txt').read().splitlines()
index = {letter: ind for ind, letter in enumerate(lines[0].split())}
scoringMatrix = list(map(lambda x: list(map(int, x.split()[1:])), lines[1:]))


def main():
	#scoreTrix = scoringMatrix()
	inputFile = open("input.txt", 'r')
	v = inputFile.readline().strip()
	w = inputFile.readline().strip()
	epsilon = 1
	sigma = 11
	score, vUpdate, wUpdate = affineGapPenalty(v, w, sigma, epsilon)
	output = open("output.txt", 'w')
	output.write(score)
	output.write(vUpdate)
	output.write(wUpdate)


main()    		