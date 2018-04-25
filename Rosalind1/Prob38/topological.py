

# def topologicalSort():
# 	sortedList = []
# 	nodesNoIncomingEdges = []
# 	while len(nodesNoIncomingEdges) > 0:
# 		nodesNoIncomingEdges.

from collections import deque
 
 
def kahn_topsort(graph):
    in_degree = { u : 0 for u in graph }     # determine in-degree 
    for u in graph:                          # of each node
        for v in graph[u]:
            in_degree[v] += 1
 
    Q = deque()                 # collect nodes with zero in-degree
    for u in in_degree:
        if in_degree[u] == 0:
            Q.appendleft(u)
 
    L = []     # list for order of nodes
     
    while Q:                
        u = Q.pop()          # choose node of zero in-degree
        L.append(u)          # and 'remove' it from graph
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                Q.appendleft(v)
 
    if len(L) == len(graph):
        return L
    else:                    # if there is a cycle,  
        return []    

graph_tasks = { "wash the dishes" : ["have lunch"],
                "cook food" : ["have lunch"],
                "have lunch" : [],
                "wash laundry" : ["dry laundry"],
                "dry laundry" : ["fold laundry"],
                "fold laundry" : [] }
graph_tasks2 = {"0" : ["1", "2"], 
				"2" : ["3"],   
				"1" : ["4"], 
				"3" : ["4"]
				}


order = kahn_topsort(graph_tasks2)
for task in order:
	print(task)

# def topological(graph):
# 	unmarkedNodes = graph
# 	while len(unmarkedNodes)>0:




# def topologicalSort(unsortedGraph):
# 	sortedGraph = []
# 	unsortedGraph = dict(unsortedGraph)
# 	for node, edges in unsortedGraph.items():
# 		for edge in edges:
# 			if edge in unsortedGraph:
# 				break
# 			else:
# 				del unsortedGraph[node]
# 				sortedGraph.append((node,edges))
# 	#print sortedGraph
# 	return sortedGraph


# print(topologicalSort([(2, []),
#                   (5, [11]),
#                   (11, [2, 9, 10]),
#                   (7, [11, 8]),
#                   (9, []),
#                   (10, []),
#                   (8, [9]),
#                   (3, [10, 8])])

