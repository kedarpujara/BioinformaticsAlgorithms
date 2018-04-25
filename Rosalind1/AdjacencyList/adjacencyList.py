class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

class Graph:
	vertices = {}
	
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:

			self.vertices[u].add_neighbor(v)
			self.vertices[v].add_neighbor(u)
			return True
		else:
			return False
			
	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors))

def suffixs(string):
	length = len(string)
	suffix = string[1:length]
	return suffix

def prefixs(string):
	length = len(string)
	prefix = string[0:length-1]
	return prefix


def adjacentNeighbors(patterns):
	leftList = []
	rightList = []
	for string1 in patterns:
		for string2 in patterns:
			if suffixs(string1) == prefixs(string2):
				leftList.append(string1)
				rightList.append(string2)
				break
	return leftList, rightList


def main():
	inputFile = open("input2.txt","r")
	patterns = []
	for line in inputFile:
		patterns.append(line.strip())
	leftList, rightList = adjacentNeighbors(patterns)
	output = open("output.txt", 'w')
	for i in range(len(leftList)):
		output.write(leftList[i] + " -> " + rightList[i] + "\n") 





g = Graph()
inputFile = open("input2.txt","r")
patterns = []
for line in inputFile:
	patterns.append(line.strip())
leftList, rightList = adjacentNeighbors(patterns)

for i in range(len(leftList)):
	g.add_vertex(Vertex(leftList[i]))

g.print_graph()

