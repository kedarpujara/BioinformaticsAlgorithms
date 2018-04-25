def topologicalSort(edgeList) :
	edgeSet = set([tuple(i) for i in edgeList])
	
	nodeList = list()
	
	fromNodeList, toNodeList = zip(* edgeSet)
	sourceSet = set(fromNodeList) - set(toNodeList)
	
	while len(sourceSet) != 0 :
		fromNode = sourceSet.pop()
		nodeList.append(fromNode)
		
		fromSelection = [e for e in edgeSet if e[0] == fromNode]
		for edge in fromSelection :			
			toNode = edge[1]
			edgeSet.discard(edge)
						
			toSelection = [e for e in edgeSet if e[1] == toNode]
			if len(toSelection) == 0 :
				sourceSet.add(toNode)

	return nodeList


def main():
	inputFile = open("input3.txt", 'r')
	outgoing = []
	incoming = []
	for line in inputFile:
		edge = line.split(" -> ")
		multiIncome = edge[1].split(',')	
		for i in range(len(multiIncome)):
			outgoing.append(edge[0])
			incoming.append(multiIncome[i].strip())											
	graph = zip(outgoing, incoming)
	orderGraph = topologicalSort(graph)
	print(', '.join(map(str,orderGraph)))

main()


u = [
	['a', 'b'], # a -> b, etc.
	['a', 'c'],
	['b', 'e'],
	['c', 'd'],
	['b', 'd'],
	['e', 'f'],
	['c', 'f'],
]
