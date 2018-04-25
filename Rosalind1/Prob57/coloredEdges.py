def coloredEdges(P):
	edges = []
	for chromosome in P:
		nodes = chromosomeToCycle(chromosome)
		for j in range(0,len(chromosome)):
			if j == 0:
				edges.append( (nodes[0], nodes[1]))
			else:
				edges.append( (nodes[2*j], nodes[2*j+1]) )
	print edges
	return edges


def chromosomeToCycle(chromosome):

	nodes = [0 for i in range(2*len(chromosome) + 1)]

	for j in range(len(chromosome)):
		i = int(chromosome[j][1:])
		sign = chromosome[j][0]
		if j == 0:
			if sign == '+':
				nodes[j] = 2*i - 1
				nodes[j+1] = 2*i
			else: 
				nodes[j] = 2*i
				nodes[j+1] = 2*i - 1
			continue
		if sign == '+':
			nodes[2*j] = 2*i -1
			nodes[2*j+1] = 2*i
		else:
			nodes[2*j] = 2*i
			nodes[2*j+1] = 2*i-1
	del nodes[-1]
	return nodes

def main():
	inputFile = open('input.txt', 'r')

	line = inputFile.readline().rstrip(')\n').lstrip('(').split(')(')
	edges = []
	for edge in line:
		edges.append(edge.split(' '))
	
	coloredEdges(edges)

main()

