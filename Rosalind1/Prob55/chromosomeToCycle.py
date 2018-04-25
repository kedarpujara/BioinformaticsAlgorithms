def chromosomeToCycle(chromosome):
	#nodes = [0]*((len(chromosome)*2)-1)
	nodes = []
	chromosomeUpdate = []
	for i in range(0, len(chromosome)):
		if chromosome[i][0] == '+':
			chromosomeUpdate.append(int(chromosome[i][1]))
		else:
			chromosomeUpdate.append(-1 * int(chromosome[i][1]))


	for j in range(0,len(chromosomeUpdate)):
		i = chromosomeUpdate[j]
		if i > 0:
			#nodes[2*j - 1] = 2*i - 1
			#nodes[2*j] = 2*i
			nodes.append(2*i - 1)
			nodes.append(2*i)

		else:
			#nodes[2*j - 2] = -2*i 
			#nodes[2*j - 1] = -2*i - 1	
			nodes.append(-2*i)
			nodes.append(-2*i - 1)
	print nodes
	return nodes


def main():
	inputF = open('input4.txt')
	chromosome = inputF.readline().translate(None, "(){}<>").strip().split(' ')
	nodes = chromosomeToCycle(chromosome)
	output = open("output.txt", 'w')


main()
