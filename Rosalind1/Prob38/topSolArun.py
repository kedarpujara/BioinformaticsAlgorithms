def longestpath(start, sink, edges):
	order = topOrdering(start,sink,edges)
	score = {}
	parents = {}
	for edge in edges:
		s = edge.split(":")
		e = s[0].split("->")
		if e[1] in parents:
			parents[e[1]].append((e[0],s[1]))
		else:
			parents[e[1]] = [(e[0],s[1])]
		if e[0] not in parents:
			parents[e[0]] = []
	for node in order:
		if node == start:
			score[node] = 0
		else:
			score[node] = -100000000
	prev = {}
	for node in order:
		if parents[node] == []:
			continue
		else:
			for i in parents[node]:
				score[node] = max(score[node], score[i[0]] + int(i[1]))
				if (score[node] == score[i[0]] + int(i[1])):
					prev[node] = i[0]
	path = sink
	curr = sink
	while curr != start:
		path = prev[curr] + "->" + path
		curr = prev[curr]
	return path, score[sink]

def topOrdering(source, sink, edges):
	parents = {}
	for pair in edges:
		edgeWeight = pair.split(":")
		edge = edgeWeight[0].split("->")
		outgoing = edge[0]
		incoming = edge[1]
		if incoming in parents:
			parents[incoming].append(outgoing)
		else:
			parents[incoming] = [outgoing]
		if outgoing not in parents:
			parents[outgoing] = []
	order = [source]
	while parents:
		TBR = []
		for key in parents:
			if set(parents[key]) <= set(order):
				order.append(key)
				TBR.append(key)
		for key in TBR:
			parents.pop(key)
	return order

#filename = raw_input()
f = open("input.txt", "r")
start = f.readline().strip()
sink = f.readline().strip()
edges = []
for line in f:
	edges.append(line.strip())
path, score = longestpath(start, sink, edges)
output = open("output.txt", "w")
output.write(str(score) +'\n')
output.write(path)