from collections import defaultdict

def twoBreakDist(P, Q):
    graph = defaultdict(list)
    for cycle in P+Q:
        for i in range(len(cycle)):
            graph[cycle[i]].append(-1*cycle[(i+1) % len(cycle)])
            graph[-1*cycle[(i+1) % len(cycle)]].append(cycle[i])

    compCount = 0
    notEmpty = set(graph.keys())
    while notEmpty:
        compCount += 1
        queue = {notEmpty.pop()}
        while queue:
            current = queue.pop()
            new_nodes = {node for node in graph[current] if node in notEmpty}
            queue |= new_nodes
            notEmpty -= new_nodes
    return sum(map(len,P)) - compCount

def main():
    with open('input4.txt') as inputFile:
        P, Q = [line.strip().lstrip('(').rstrip(')').split(')(') for line in inputFile]    
    P = [map(int, cycle.split()) for cycle in P]
    Q = [map(int, cycle.split()) for cycle in Q]

    dist = twoBreakDist(P, Q)
    output = open('output.txt','w')
    output.write(str(dist))
    
main()