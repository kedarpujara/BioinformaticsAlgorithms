def lastToFirst(transform, ind):
	visited = {}
	for i in range(len(transform)):
		if transform[i] not in visited:
			visited[transform[i]] = 1
			transform[i] = (transform[i], 1)
		else:
			visited[transform[i]] += 1
			transform[i] = (transform[i], visited[transform[i]])
	transformSort = sorted(transform)
	return transformSort.index(transform[ind])

def main():
	inputFile = open('input2.txt')
	transform = list(inputFile.readline().strip())
	i = int(inputFile.readline().strip())
	lastToFirstPos = lastToFirst(transform, i)
	print lastToFirstPos

main()