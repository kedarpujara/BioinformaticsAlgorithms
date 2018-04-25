class trieConstruct(object):
    def __init__ (self,patterns):
        self.seq = {}
        self.tree= lambda parent, d: {'d': d,'childNodes': [], 'parentNode': parent,}
        self.nodes= { 1 : self.tree( 0 , 0) }

        for pattern in patterns:
            self.patternTrie(pattern)

    def patternTrie(self, pattern):
        insertNode,insertPattern= self.trieIndex(pattern)
        for i in range(0, len(insertPattern)):
            nodes=len(self.nodes)+1
            self.nodes[insertNode]['childNodes'].append(nodes)
            self.seq[insertNode, nodes]=insertPattern[i]
            self.nodes[nodes]= self.tree(insertNode, self.nodes[insertNode]['d']+1)
            insertNode = nodes

    def trieIndex(self, pattern, curr=1):
        for node in self.nodes[curr]['childNodes']:
            if self.seq[curr, node]==pattern[0]:
                return self.trieIndex( pattern[1:], node)

        return curr,pattern

        

def trieConstruction():
    inputFile = open('input5.txt')
    trieData = []
    for data in inputFile:
        trieData.append(data.strip())
    trie = trieConstruct(trieData)
    trieConstruction = sorted(trie.seq.items(), key=lambda sort:sort[0][1])
    output = open("output.txt","w")
    for i in trieConstruction:
        output.write(str(i[0][0] -1) + "->" + str(i[0][1] -1) + ":"+i[1] + "\n")
    

trieConstruction()