
def topologicalSort(edge_list) :
	# edge_set is consummed, need a copy
	edge_set = set([tuple(i) for i in edge_list])
	
	# node_list will contain the ordered nodes
	node_list = list()
	
	# source_set is the set of nodes with no incomming edges
	node_from_list, node_to_list = zip(* edge_set)
	source_set = set(node_from_list) - set(node_to_list)
	
	while len(source_set) != 0 :
		# pop node_from off source_set and insert it in node_list
		node_from = source_set.pop()
		node_list.append(node_from)
		
		# find nodes which have a common edge with node_from
		from_selection = [e for e in edge_set if e[0] == node_from]
		for edge in from_selection :			
			node_to = edge[1]
			edge_set.discard(edge)
						
			to_selection = [e for e in edge_set if e[1] == node_to]
			if len(to_selection) == 0 :
				source_set.add(node_to)
				

	return node_list

#def topological()


# def longestPath(graph):
# 	sortedGraph = topologicalSort(graph)
# 	dist = []
# 	totalDist = 0

# 	for i in range(len(sortedGraph)):
# 		totalDist = 

def main():
	inputFile = open("input.txt", "r")
	sourceNode = inputFile.readline().strip()
	sinkNode = inputFile.readline().strip()
	graphList = []
	#for line in inputFile:


def main():
	inputFile = open("input.txt", 'r')
	outgoing = []
	incoming = []
	for line in inputFile:
		edge = inputFile.readline().split(" -> ")
		outgoing.append(edge[0])
		incoming.append(edge[0])

	graph = zip(outgoing, incoming)
	print graph()

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

# 1 -> 2
# 2 -> 3
# 4 -> 2
# 5 -> 3

w = [
	['1', '2'],
	['2', '3'],
	['4', '2'],
	['5', '3'],

	]

v = [
	['0', '1'],
	['0', '2'],
	['2', '3'],
	['1', '4'],
	['3', '4'],

]


#print(topologicalSort(w))
#['a', 'c', 'b', 'e', 'd', 'f']
