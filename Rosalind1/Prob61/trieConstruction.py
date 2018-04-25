class Trie(object):
    def __init__(self, patterns):
        self.createNode = lambda p, d: {'parent':p, 'children':[], 'depth':d, 'end':False}

        self.nodes = {1:self.createNode(0,0)}
        self.edges = {}

        for pattern in patterns:
            self.addWord(pattern)

    def addWord(self, curr):
        insertNode, insertSubstring = self.insertLocation(curr)

        for i in range(len(insertSubstring)):

            newNode = len(self.nodes) + 1

            self.nodes[newNode] = self.createNode(insertNode, self.nodes[insertNode]['depth']+1)
            self.nodes[insertNode]['children'].append(newNode)

            self.edges[insertNode, newNode] = insertSubstring[i]

            insertNode = newNode

        self.nodes[insertNode]['end'] = True

    def insertLocation(self, pattern, curr=1):
        if pattern == '':
            return curr, pattern

        for child in self.nodes[curr]['children']:
            if self.edges[curr, child] == pattern[0]:
                return self.insertLocation(pattern[1:], child)

        return curr, pattern

def trieEdges(words):
    trie = Trie(words)

    adjFormat = lambda item: ' '.join(map(str,item[0]))+':'+item[1]

    return map(adjFormat, trie.edges.items())


def main():
    inputFile = open('input.txt')
    patterns = []
    for line in inputFile:
        patterns.append(line.strip())

    adjList = trieEdges(patterns)
    tempList = []
    printList = []
    firstList = []
    maxVal = 0
    for node in adjList:
        tempList.append(node.split())

    for i in range(len(tempList)-1):
        firstList.append(int(tempList[i][0]))
        if maxVal < int(tempList[i][0]):
            maxVal = int(tempList[i][0])
        else:
            continue
    index = firstList.index(maxVal)
    #tempList.pop(index)
    tempList = sorted(tempList)
    #print index
    for node in tempList:
        newString = node[0] + "->" + node[1]
        printList.append(newString)

    print maxVal
    output = open("output.txt","w")
    output.write('\n'.join(printList))

main()