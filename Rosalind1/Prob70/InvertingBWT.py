def invertBWT(bwt):
	visited = {}
	for i in range(len(bwt)):
		if bwt[i] not in visited:
			visited[bwt[i]] = 1
			bwt[i] = (bwt[i],1)
		else:
			visited[bwt[i]] += 1 
			bwt[i] = (bwt[i],visited[bwt[i]])
	sortVisited = sorted(bwt)
	invertString = " "
	curr = sortVisited[0]
	while invertString[-1] != "$":
		invertString += sortVisited[bwt.index(curr)][0]
		curr = sortVisited[bwt.index(curr)]
	return invertString

def main():
	inputFile = open('input2.txt')
	bwt = list(inputFile.readline().strip())
	inverseString = invertBWT(bwt)
	output = open('output.txt','w')
	output.write(inverseString[1:])

main()
