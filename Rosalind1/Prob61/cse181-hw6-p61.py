class Trie(object):
    
    def __init__ (self,patterns):

        self.letter = {}
        self.nodesInit= lambda parent, d: {'d': d,'childNodes': [], 'parentNode': parent,}
        self.val= { 1 : self.nodesInit( 0 , 0) }

        for i in patterns:
            self.patternAppend(i )


    def patternIndex(self, patternA, nval=1):

        for i in self.val[nval]['childNodes']:

            if self.letter[nval, i]==patternA[0]:
                return self.patternIndex( patternA[1:], i)

        return nval,patternA

    def patternAppend(self, pattern):

        nodeI,subI= self.patternIndex(pattern)
        for i in range(0, len(subI)):

            val=len(self.val)+1
            self.letter[nodeI, val]=subI[i]

            self.val[nodeI]['childNodes'].append(val)

            self.val[val]= self.nodesInit(nodeI, self.val[nodeI]['d']+1)
            
            nodeI=val
        



def rTrieConstruction(input):

    file1 = open(input)
    data1 = [i.strip() for i in file1.readlines()]
    trie=Trie(data1)
    list1 = []
    list1=sorted(trie.letter.items(), key=lambda x:x[0][1])
    for i in list1:
        print str(i[0][0] -1) + "->" + str(i[0][1] -1) + ":"+i[1]
    

rTrieConstruction("input2.txt")