def euler(graph):
    eulerCycle = []
    edges = sum(len(graph[i]) for i in graph)
    num = 0
    while True:
        eulerCycle.extend(cycle(graph, num))
        if len(eulerCycle) == edges+1:
            return eulerCycle
        else:
            for i in eulerCycle:
                if len(graph[i]) != 0:
                    eulerCycle = eulerCycle[eulerCycle.index(i):] + eulerCycle[1:eulerCycle.index(i)]
                    num = i
                    break

def cycle(adjList, index):
    nodesChecked = [index]
    curr = adjList[index]
    
    while 1>0:
        for i in curr:
            nodesChecked.append(i)
            curr = adjList[i]
            adjList[index].remove(i)
            index = i
            break
        else:
            return nodesChecked
def main():
	patterns = open('input5.txt').read().splitlines()
	eulerDict = {}
	for val in patterns:
		splitVal = val.split()
		eulerDict[int(splitVal[0])] = list(map(int, splitVal[2].split(',')))

	output = open('output3.txt','w')
	
	newString = ""
	results = euler(eulerDict)
	for i in results:
		output.write((str(results[i]) + '->').replace('\n',''))

main()