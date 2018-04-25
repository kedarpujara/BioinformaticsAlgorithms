def overlapAlignment(string1, string2):
    len1 = len(string1)
    len2 = len(string2)

    dist = [[0 for repeat_j in range(len2+1)] for repeat_i in range(len1+1)]
    backtrack = [[0 for repeat_j in range(len2+1)] for repeat_i in range(len1+1)]
    maxScore = -3*(len1 + len2)

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            score = [dist[i-1][j-1] + [-2, 1][string1[i-1] == string2[j-1]], dist[i-1][j] - 2, dist[i][j-1] - 2]
            dist[i][j] = max(score)
            backtrack[i][j] = score.index(dist[i][j])

            if i == len1 or j == len2:
                if dist[i][j] > maxScore:
                    maxScore = dist[i][j]
                    maxIndex = (i, j)
    i, j = maxIndex
    overlap1, overlap2 = string1[:i], string2[:j]
    indel = lambda diff, i: diff[:i] + '-' + diff[i:]

    while i*j != 0:
        if backtrack[i][j] == 1:
            i -= 1
            overlap2 = indel(overlap2, j)
        elif backtrack[i][j] == 2:
            j -= 1
            overlap1 = indel(overlap1, i)
        else:
            i -= 1
            j -= 1
    overlap1, overlap2 = overlap1[i:], overlap2[j:]

    return str(maxScore), overlap1, overlap2


def main():
    inputFile = open("input3.txt", "r")
    string1 = inputFile.readline().strip()
    string2 = inputFile.readline().strip()


    alignment = overlapAlignment(string1, string2)

    output = open("output.txt", "w")
    output.write('\n'.join(alignment))

main()