def manhattanTourist(n,m,down,right):

	dist = [[0 for y in range(m+1)] for x in range(n+1)]
	backtrack = [[0 for y in range(m+1)] for x in range(n+1)]
	for i in range(1,n+1):
		dist[i][0] = dist[i-1][0] + down[i-1][0]

	for j in range(1,m+1):
		dist[0][j] = dist[0][j-1] + right[0][j-1]

	for i in range(1,n+1):
		for j in range(1,m+1):
			dist[i][j] = max(dist[i-1][j] + down[i-1][j], dist[i][j-1] + right[i][j-1])

			if dist[i][j] == dist[i-1][j]:
				backtrack[i][j] = "down"
			elif dist[i][j] == dist[i][j-1]:
				backtrack[i][j] = "right"
			elif dist[i][j] == dist[i-1][j-1] + 1 && string1[i] == string2[j]:
				backtrack[i][j] = "diag"
			


	return dist[n][m]




def main():
	inputFile = open("input3.txt","r")
	n = int(inputFile.readline().strip())
	m = int(inputFile.readline().strip())
	down = []
	right = []
	for i in range(n):
		down.append(map(int,inputFile.readline().split(" ")))
	inputFile.readline()

	for j in range(0,(n+1)):
		right.append(map(int,inputFile.readline().split(" ")))
	dist = manhattanTourist(n,m,down,right)
	print dist

main()