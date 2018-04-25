def bwMatching(bwt, patterns):
	visited = {}
	for i in range(len(bwt)):
		if bwt[i] not in visited:
			visited[i] = 1
			bwt[i] = (bwt[i], 1)
		else:
			visited[bwt[i]] += 1
			bwt[i] = (bwt[i], visited[bwt[i]])
	sortedBWT = sorted(bwt)
	top = 0
	bottom = len(bwt) - 1
	while top <= bottom:
		if patterns:
			symbol = patterns[-1]
			patterns = patterns[:-1]
			if symbol in [x[0] for x in bwt[top:bottom+1]]:
				for topIndex in range(top, bottom+1):
					if bwt[topIndex][0] == symbol:
						break
				for bottomIndex in range(bottom, top-1, -1):
					if bwt[bottomIndex][0] == symbol:
						break

				top = sortedBWT.index(bwt[topIndex])
				bottom = sortedBWT.index(bwt[bottomIndex])
			else:
				return 0
		else:
			return bottom - top + 1





def main():
	inputFile = open('input.txt')
	bwt = list(inputFile.readline().strip())
	patterns = inputFile.readline().strip().split(' ')	
	
	bwMatch = [str(bwMatching(bwt, pattern)) for pattern in patterns]

	output = open('output.txt','w')
	output.write((' ').join(bwMatch))

main()