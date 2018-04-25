def multipleLCS(v, w, u):

    len1 = len(v)
    len2 = len(w)
    len3 = len(u)

    dist = [[[0 for k in range(len3+1)] for j in range(len2+1)] for i in range(len1+1)]
    backtrack = [[[0 for k in range(len3+1)] for j in range(len2+1)] for i in range(len1+1)]

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            for k in range(1, len3+1):
                scores = [dist[i-1][j-1][k-1] + int(v[i-1] == w[j-1] == u[k-1]), dist[i-1][j][k], dist[i][j-1][k], dist[i][j][k-1], dist[i-1][j][k-1], dist[i][j-1][k-1]]
                backtrack[i][j][k], dist[i][j][k] = max(enumerate(scores), key=lambda p: p[1])

    indel = lambda word, i: word[:i] + '-' + word[i:]

    vUpdated, wUpdated, uUpdated = v, w, u

    i, j, k = len1, len2, len3
    maxScore = dist[i][j][k]

    while i != 0 and j != 0 and k != 0:
        if backtrack[i][j][k] == 1:
            i -= 1
            wUpdated = indel(wUpdated, j)
            uUpdated = indel(uUpdated, k)
        elif backtrack[i][j][k] == 2:
            j -= 1
            vUpdated = indel(vUpdated, i)
            uUpdated = indel(uUpdated, k)
        elif backtrack[i][j][k] == 3:
            k -= 1
            vUpdated = indel(vUpdated, i)
            wUpdated = indel(wUpdated, j)
        elif backtrack[i][j][k] == 4:
            i -= 1
            j -= 1
            uUpdated = indel(uUpdated, k)
        elif backtrack[i][j][k] == 5:
            i -= 1
            k -= 1
            wUpdated = indel(wUpdated, j)
        elif backtrack[i][j][k] == 6:
            j -= 1
            k -= 1
            vUpdated = indel(vUpdated, i)
        else:
            i -= 1
            j -= 1
            k -= 1

    while len(vUpdated) != max(len(vUpdated),len(wUpdated),len(uUpdated)):
        vUpdated = indel(vUpdated, 0)
    while len(wUpdated) != max(len(vUpdated),len(wUpdated),len(uUpdated)):
        wUpdated = indel(wUpdated, 0)
    while len(uUpdated) != max(len(vUpdated),len(wUpdated),len(uUpdated)):
        uUpdated = indel(uUpdated, 0)

    return str(maxScore), vUpdated, wUpdated, uUpdated

def main():
    inputFile = open("input3.txt", 'r')
    string1 = inputFile.readline().strip()
    string2 = inputFile.readline().strip()
    string3 = inputFile.readline().strip()    
    maxScore, v,w,u = multipleLCS(string1, string2, string3)
    print(maxScore)
    print(v)
    print(w)
    print(u)

main()