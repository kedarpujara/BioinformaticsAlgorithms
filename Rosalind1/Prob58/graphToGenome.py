def graphToGenome(genome):
	#print genome
	list1 = []
	listV = []
	listE = []

	for i in range(len(genome)*2):
		listE.append(0)
		
	for i in genome:
		listE[i[1]-1] = i[0]-1
		listE[i[0]-1] = i[1]-1

	#print "listE: ", listE
	for i in genome:
		orig = i[0]
		#print "orig: ", orig, "listV: ", listV
		if orig in listV:
			continue
		if orig%2 == 0:
			closing = orig-1
		else:
			closing = orig+1

		p = []
		j = 0
		while(True):			
			if (orig%2 == 0):
				
				p.append(orig/2)
			else:
				
				p.append(-(orig+1)/2)
			dest = listE[orig-1]+1
			j = j +1
			listV.append(dest)
			if dest == closing:
				list1.append(p)
				break
			if dest%2 == 0:
				orig = dest -1
			else:
				orig = dest + 1

			listV.append(orig)
	return list1

def main():
	file1 = open('input3.txt')
	pfile1 = file1.readlines()[0]
	pfile1 = pfile1.replace(")(", "),(")
	pfile1 =  pfile1.replace(" ", "")
	P = eval("[%s]" % pfile1)
	graphToGenome(P)
	f = open('ot.txt')
	line = f.readline().replace('[', '(').replace(']',')').replace(', ', ' ')
	print line
	# for graph in graphG:
	# 	for i in range(len(graph)):
	# 		print graph[i]

main()
# def graphToGenome(genomeGraph):
# 	P = []
# 	for cycle in genomeGraph:
# 		chromosome = cycleToChromosome(cycle)
# 		P.append(chromosome)
# 	print P
# 	return P


# def cycleToChromosome(Nodes):
# 	list1 = []
# 	listR = []
# 	for i in range(len(Nodes)/2):
# 		if Nodes[2*i] < Nodes[2*i+1]:
# 			val = i+1
# 		else:
# 			val = -(i+1)
# 		list1.append(val)
# 	for i in list1:
# 		if i >0:
# 			listR.append("+"+str(i))
# 		if i<0:
# 			listR.append(str(i))

# 	print "(" + " ".join(listR) + ")"
# 	return list1

# def main():
# 	inputFile = open('input.txt')
# 	line = inputFile.readline().rstrip(')\n').lstrip('(').split(')(')
# 	edges = []
# 	for edge in line:
# 		edges.append(edge.split(' '))

# def rCycleToChromosome(input):
# 	file1 = open(input)
# 	pfile1 = file1.readlines()[0].strip()
# 	list1 = []
# 	for i in pfile1[1:-1].split():
# 		list1.append(int(i))
# 	cycleToChromosome(list1)


#rCycleToChromosome("inputDataset.txt")






# def cycleToChromosome(nodes):
# 	nodeNum = []
# 	chromosome = []
# 	for i in range(len(nodes)):
# 		nodeNum.append(int(nodes[i]))

# 	for j in range(1, len(nodeNum)/2):
# 		if nodeNum[2*j - 1] < nodeNum[2*j]:
# 			chromosome.append(nodeNum[2*j]/2)
# 		else:
# 			chromosome.append(-1*nodeNum[2*j-1]/2)

# 	print chromosome
# 	return chromosome

# def main():
