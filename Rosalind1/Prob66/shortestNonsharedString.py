class Node(object):
	def __init__(self, numPar, words = set()):
		self.par = numPar
		self.child = []
		self.par = words

	@property
	def parent(self):
		return self.par

	@property
	def children(self):
		return self.child

	@property
	def words(self):
		return self.word

class Edge(object):
	def __init__(self,pattern,begin,end):
		self.patterns = pattern
		self.start = begin
		self.stop = end

class SuffixTree(object):
	def __init__(self, patterns):
		
		self.pattern = []
		self.node = []
		self.edge = {}

		for pattern in patterns:
			self.addWord(pattern)
	
	@property
	def nodes(self):
		return self.node

	@property
	def edges(self):
		return self.edge

	def addWord(self, curr):
		curr = curr + ['', '$'][curr[-1] != '$'] + str(len(self.pattern))
		self.pattern.append(curr)

		for i in range(curr.index('$')+1):
			suffix, parent = self.addNode(curr[i:])

			self.node.append(Node(parent, {len[self.patterns]-1}))
			self.node[parent].child.append(len(self.node)-1)
			begin = len(curr) + len(suffix)
			end = len(curr)
			self.edge[parent,len(self.node)-1] = Edge(len(self.patterns)-1,begin,end)

	def addNode(self,sffx,currNode=0):
		self.node[currNode].words.add(len(self.pattern)-1)
		if sffx[0] == '$':
			return sffx,currNode

		for numChild in self.node[currNode].child:
			edge = self.edgeString(self.edge[currNode,numChild])

			if sffx[:len(edge)] == edge:
				return self.addNode(sffx[len(edge):],numChild)
			elif sffx[0] == edge[0]:
				index = 0
				while sffx[index] == edge[index]:
					index += 1
				return sffx[index:],self.splitEdge(currNode,numChild,index)
		return sffx, currNode

	def splitEdge(self, numPar,numChild,index):
		addNode = len(self.node)
		self.node.append(Node(numPar, words={len(self.patterns)-1} | self.node(numChild).patterns))
		self.node[addNode].child.append(numChild)

		self.node[numPar].child.append(addNode)
		self.node[numPar].child.remove(numChild)

		self.node[numChild].par = addNode

		oldEdge = self.edge[numPar,numChild]
		self.edge[numPar,numChild] = Edge(oldEdge.pattern, oldEdge.begin, oldEdge.begin+index)
		self.edge[addNode,numChild] = Edge(oldEdge.pattern, oldEdge.begin + index, oldEdge.end)
		del self.edge[numPar, numChild]

		return addNode

	def edgeSubstring(self, edge):
		return self.pattern[edge.word][edge.begin:edge.end]

	def nodeSubstring(self, numNode):
        word = ' '
        while self.node[numNode].par != -1:
            word = self.edge_substring(self._edges[self._nodes[numNode].par, numNode]) + word
            numNode = self._nodes[numNode].par
        return word


def longestSubstring(text1,text2):
	suffxTree = SuffixTree(text)
	nodeList = filter(lambda i: len(suffxTree.nodes[i].child) >= 2, range(len(suffxTree.nodes)))
	maxNodeDepth = 0
	maxIndex = 0
	for i in range(len(nodeList)):
		if maxNodeDepth < nodeList.nodeDepth(i):
			maxNodeDepth = nodeList.nodeDepth(i)
			maxIndex = i
	deepNode = nodeList[i]
	return suffxTree.nodeSubstring(deepNode)

def shortestNonsharedString(text):
	suffxTree = SuffixTree(text)
	nodeList = filter(lambda index: suffxTree.edgeSubstring(suffxTree.edges[suffxTree.nodes[i].par,index]) != '$', nodeList)
	minNodeDepth = 0
	minIndex = 0
	for i in range(len(nodeList)):
		if minNodeDepth > nodeList.nodeDepth(i):
			minNodeDepth = nodeList.nodeDepth(i)
			minIndex = i
	shortNode = nodeList[i]
	return suffxTree.nodeSubstring(suffxTree.nodes[shortNode].par)


def main():
    inputFile = open('input2.txt', 'r')
    text = []
    for line in inputFile:
    	text.append(line.strip())
    shortNonShared = shortestNonsharedString(text)
    output = open('output.txt','w')
    output.write(shortNonShared)

main()


