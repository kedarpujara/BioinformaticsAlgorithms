def localAlignment(string1, string2, scoringMatrix, sigma):
    len1 = len(string1)
    len2 = len(string2)

    dist = [[0 for j in xrange(len2+1)] for i in xrange(len1+1)]
    backtrack = [[0 for j in xrange(len2+1)] for i in xrange(len1+1)]
    maxScore, iMax, jMax = -1, 0, 0



    # Fill in the Score and Backtrack matrices.
    for i in xrange(1, len1+1):
        for j in xrange(1, len2+1):
            scores = [dist[i-1][j] - sigma, dist[i][j-1] - sigma, dist[i-1][j-1] + scoringMatrix[string1[i-1], string2[j-1]], 0]
            dist[i][j] = max(scores)
            backtrack[i][j] = scores.index(dist[i][j])

            if S[i][j] > maxScore:
                maxScore, iMax, jMax = dist[i][j], i, j

    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    i,j = iMax, jMax

    v_aligned, w_aligned = v[:i], w[:j]

    while backtrack[i][j] != 3 and i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1

    v_aligned = v_aligned[i:]
    w_aligned = w_aligned[j:]

    return str(maxScore), v_aligned, w_aligned


def scoringMatrix():
    lines = open('scoringMatrix.txt').read().splitlines()
    index = {letter: ind for ind, letter in enumerate(lines[0].split())}
    PAM = list(map(lambda x: list(map(int, x.split()[1:])), lines[1:]))
    #print PAM
    return PAM

def main():
    inputFile = open("input.txt")
    string1 = inputFile.readline().strip()
    string2 = inputFile.readline().strip()

    scoring = scoringMatrix()

    alignment = localAlignment(string1, string2, scoring, 5)

    print '\n'.join(alignment)
    with open('output.txt', 'w') as output_data:
        output_data.write('\n'.join(alignment))

main()