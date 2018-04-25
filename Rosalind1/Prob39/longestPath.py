def topologicalOrder(source, sink, edges):
	candidates = {}
	for pair in edges:
		edgeWeight = pair.split(":")
		edge = edgeWeight[0].split("->")
		outgoing = edge[0]
		incoming = edge[1]
		if incoming in candidates:
			candidates[incoming].append(outgoing)
		else:
			candidates[incoming] = [outgoing]
		if outgoing not in candidates:
			candidates[outgoing] = []
	topOrder = [source]
	while candidates:
		tpo = []
		for key in candidates:
			if set(candidates[key]) <= set(topOrder):
				topOrder.append(key)
				tpo.append(key)
		for key in tpo:
			candidates.pop(key)
	return topOrder

def longestPath(source, sink, edges):
	topOrder = topologicalOrder(source, sink, edges)
	score = {}
	candidates = {}
	for pair in edges:
		edgeWeight = pair.split(":")
		edge = edgeWeight[0].split("->")
		outgoing = edge[0]
		incoming = edge[1]
		weight = edgeWeight[1]

		if incoming in candidates:
			candidates[incoming].append((outgoing,weight))
		else:
			candidates[incoming] = [(outgoing,weight)]
		if outgoing not in candidates:
			candidates[outgoing] = []
	for node in topOrder:
		if node == source:
			score[node] = 0
		else:
			score[node] = -100000000
	prevNode = {}
	for node in topOrder:
		if candidates[node] == []:
			continue
		else:
			for i in candidates[node]:
				score[node] = max(score[node], score[i[0]] +  int(i[1]))
				if (score[node] == score[i[0]] + int(i[1])):
					prevNode[node] = i[0]
	longestPath = sink
	currNode = sink
	while currNode != source:
		longestPath = prevNode[currNode] + "->" + longestPath
		currNode = prevNode[currNode]
	return longestPath, score[sink]


def main():
	f = open("input2.txt", "r")
	start = f.readline().strip()
	sink = f.readline().strip()
	edges = []
	for line in f:
		edges.append(line.strip())
	path, score = longestPath(start, sink, edges)
	output = open("output.txt", "w")
	output.write(str(score) +'\n')
	output.write(path)


main()


