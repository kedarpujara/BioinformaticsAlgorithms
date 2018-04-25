def cycleToChromosome(Nodes):
	list1 = []
	listR = []
	for i in range(len(Nodes)/2):
		if Nodes[2*i] < Nodes[2*i+1]:
			val = i+1
		else:
			val = -(i+1)
		list1.append(val)
	for i in list1:
		if i >0:
			listR.append("+"+str(i))
		if i<0:
			listR.append(str(i))

	print "(" + " ".join(listR) + ")"
	return list1

def rCycleToChromosome(input):
	file1 = open(input)
	pfile1 = file1.readlines()[0].strip()
	list1 = []
	for i in pfile1[1:-1].split():
		list1.append(int(i))
	#print list1
	cycleToChromosome(list1)


rCycleToChromosome("input2.txt")

# def cycleToChromosome(nodes):
# 	nodeNum = []
# 	chromosome = []
# 	for i in range(len(nodes)):
# 		nodeNum.append(int(nodes[i]))

# 	for j in range(0, len(nodeNum)/2):
# 		if j == 0:
# 			if nodeNum[0] < nodeNum[1]:
# 				chromosome.append(nodeNum[1]/2)
# 			else:
# 				chromosome.append(-1*nodeNum[0]/2)
# 		else:
# 			if nodeNum[2*j - 1] < nodeNum[2*j]:
# 				chromosome.append(nodeNum[2*j]/2)
# 			else:
# 				chromosome.append(-1*nodeNum[2*j-1]/2)

# 	print chromosome
# 	return chromosome




# def main():
# 	inputF = open('input.txt')
# 	chromosome = inputF.readline().translate(None, "(){}<>").strip().split(' ')
# 	cycleToChromosome(chromosome)
# 	#print chromosome

# main()
