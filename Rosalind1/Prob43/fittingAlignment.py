def fittingAlignment(string1,string2):

    len1 = len(string1)
    len2 = len(string2)

    dist = [[0 for j in range(len2+1)] for i in range(len1+1)]
    backtrack = [[0 for j in range(len2+1)] for i in range(len1+1)]

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            scores = [dist[i-1][j] - 1, dist[i][j-1] - 1, dist[i-1][j-1] + [-1, 1][string1[i-1] == string2[j-1]]]
            dist[i][j] = max(scores)
            backtrack[i][j] = scores.index(dist[i][j])

    j = len2
    i = max(enumerate([dist[row][j] for row in range(len2, len1)]),key=lambda val: val[1])[0] + len2
    maxScore = str(dist[i][j])

    fit1, fit2 = string1[:i], string2[:j]

    indel = lambda diff, i: diff[:i] + '-' + diff[i:]

    while i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            fit2 = indel(fit2, j)
        elif backtrack[i][j] == 1:
            j -= 1
            fit1 = indel(fit1, i)
        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1

    fit1 = fit1[i:]
    print fit1, fit2
    return maxScore, fit1, fit2


def main():
    inputFile = open("input4.txt")
    string1 = inputFile.readline().strip()
    string2 = inputFile.readline().strip()

    alignment = fittingAlignment(string1, string2)

    print '\n'.join(alignment)
    with open('output.txt', 'w') as output_data:
        output_data.write('\n'.join(alignment))

main()