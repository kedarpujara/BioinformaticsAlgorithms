def affineGapPenalty(v, w, scoringMatrix, sigma, epsilon):
	len1 = len(v)
	len2 = len(w)

	lower = [[0 for j in xrange(len2+1)] for i in xrange(len1+1)]
	middle = [[0 for j in xrange(len2+1)] for i in xrange(len1+1)]
	upper = [[0 for j in xrange(len2+1)] for i in xrange(len1+1)]
	backtrack = [[0 for j in range(len2+1)] for i in range(len1+1)]

	maxScore = -1
	maxI, maxJ = 0,0

	for i in range(1, len1+1):
		for j in range(1, len2+1):
			lower[i][j] = max(lower[i-1][j] - epsilon, middle[i-1][j] - sigma)
			upper[i][j] = max(upper[i][j-1] - epsilon, middle[i][j-1] - sigma)
			midScore = [lower[i][j], middle[i-1][j-1] + scoringMatrix[v[i-1], w[j-1]], upper[i][j], 0]
			middle[i][j] = max(midScore)
			backtrack[i][j] = midScore.index(middle[i][j])

			if middle[i][j] > maxScore:
				maxScore = middle[i][j]
				maxI = i
				maxJ = j


	#BACKTRACK
	i = maxI
	j = maxJ

	vUpdated = v[:i]
	wUpdated = w[:j]

	while backtrack[i][j] != 3 and (i != 0 or j != 0):
		if backtrack[i][j] == 0:
			i -= 1
		elif backtrack[i][j] == 1:
			i -= 1
			j -= 1
		elif backtrack[i][j] == 2:
			j -= 1

	vUpdated = vUpdated[i:]
	wUpdated = wUpdated[j:]

	return str(maxScore), vUpdated, wUpdated


def scoringMatrix():
	lines = open('scoringMatrix.txt').read().splitlines()
	index = {letter: ind for ind, letter in enumerate(lines[0].split())}
	PAM = list(map(lambda x: list(map(int, x.split()[1:])), lines[1:]))
	return PAM



def main():
	scoreTrix = scoringMatrix()
	inputFile = open("input.txt", 'r')
	v = inputFile.readline().strip()
	w = inputFile.readline().strip()
	epsilon = 1
	sigma = 11
	score, vUpdate, wUpdate = affineGapPenalty(v, w, scoreTrix, sigma, epsilon)
	output = open("output.txt", 'w')
	output.write(score)
	output.write(vUpdate)
	output.write(wUpdate)

main()








