def middleNode(v, w, sigma):
    len1 = len(v)
    len2 = len(w)

    dist = [[i*j*sigma for j in xrange(-1, 1)] for i in xrange(len1+1)]
    dist[0][1] = -sigma
    backtrack = [0]*(len1+1)

    index, scoreMatrix = scoringMatrix()
    for j in xrange(1, len2/2+1):
        for i in xrange(0, len1+1):
            if i == 0:
                dist[i][1] = -j*sigma
            else:
                index1 = index[v[i-1]]
                index2 = index[w[j-1]]
                scores = [dist[i-1][0] + scoreMatrix[index1][index2], dist[i][0] - sigma, dist[i-1][1] - sigma]
                dist[i][1] = max(scores)
                backtrack[i] = scores.index(dist[i][1])

        if j != len2/2:
            dist = [[row[1]]*2 for row in dist]

    return [row[1] for row in dist], backtrack


def middleEdge(v, w, sigma):
    len1 = len(v)
    len2 = len(w)
    toMiddle = middleNode(v, w, sigma)[0]
    fromMiddle, backtrack = map(lambda l: l[::-1], middleNode(v[::-1], w[::-1]+['', '$'][len2 % 2 == 1 and len2 > 1], sigma))

    scores = map(sum, zip(toMiddle, fromMiddle))
    middleMax = max(xrange(len(scores)), key=lambda i: scores[i])

    if middleMax == len(scores) - 1:
        next = (middleMax, len2/2 + 1)
    else:
        next = [(middleMax + 1, len2/2 + 1), (middleMax, len2/2 + 1), (middleMax + 1, len2/2),][backtrack[middleMax]]

    return (middleMax, len2/2), next


def scoringMatrix():
    lines = open('scoringMatrix.txt').read().splitlines()
    index = {letter: ind for ind, letter in enumerate(lines[0].split())}
    scoreMatrix = list(map(lambda x: list(map(int, x.split()[1:])), lines[1:]))
    return index, scoreMatrix



def main():
    inputFile = open('input3.txt', 'r')
    v = inputFile.readline().strip()
    w = inputFile.readline().strip()

    middle = middleEdge(v, w, 5)

    output = open("output.txt", 'w')
    output.write(' '.join(map(str, middle)))

main()