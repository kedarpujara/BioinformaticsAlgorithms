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


def deBruijnOld(patterns):
	leftList = []
	rightList = []
	for string1 in patterns:
		for string2 in patterns:
			if suffixs(string1) == prefixs(string2):
				leftList.append(string1)
				rightList.append(string2)
				break
	return leftList, rightList


def deBruijn(inputString, k):
	leftList = []
	rightList = []
	multiList = []
	for i in range(len(inputString)-k+1):
		string1 = inputString[i:i+k-1]
		string2 = inputString[i+1:i+k]
		if any(string1 in s for s in rightList):
			newString = inputString[i:i+k-1] + inputString[i+1:i+k]
			break
		leftList.append(string2)
		rightList.append(string1)
		
	return rightList, leftList

def main():
	inputFile = open("input.txt","r")
	k = int(inputFile.readline().strip())
	inputString = inputFile.readline().strip()
	leftList, rightList = deBruijn(inputString, k)
	output = open("output.txt", 'w')
	for i in range(len(leftList)):
		output.write(leftList[i] + " -> " + rightList[i] + "\n") 

main()