def euler(graph):
    path = []
    adj_list = construct_graph(graph)
    edges = sum(len(adj_list[i]) for i in adj_list)
    n = 0
    while True:
        path.extend(cycle(adj_list, n))
        if len(path) == edges+1:
            return path
        else:
            for i in path:
                #print(adj_list)
                if len(adj_list[i]) != 0:
                    path = path[path.index(i):] + path[1:path.index(i)]
                    n = i
                    #print(n)
                    break

def construct_graph(graph):
    results = {}
    for i in graph:
        x = i.split()
        results[int(x[0])] = list(map(int, x[2].split(',')))
    return results

def cycle(adj, n):
    visited = [n]
    current_node = adj[n]
    
    while True:
        for i in current_node:
                visited.append(i)
                current_node = adj[i]
                adj[n].remove(i)
                n = i
                break
        else:
            return visited

patterns = open('input.txt').read().splitlines()


results = euler(patterns)
print(results)
retString = ""
for i in results:
    retString += str(results[i]) + "->"
    print retString

#print(*results, sep='->')