def editDistance(string1,string2):
    len1 = len(string1)
    len2 = len(string2)

    matrix = [[0 for j in xrange(len2+1)] for i in xrange(len1+1)]
    for i in range(1,len1+1):
        matrix[i][0] = i
    for j in range(1,len2+1):
        matrix[0][j] = j

    for i in xrange(1,len1+1):
        for j in xrange(1,len2+1):
            if string1[i-1] == string2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+1)
    print matrix
    return matrix[len1][len2]


def main():
    inputFile = open("input.txt")
    string1 = inputFile.readline().strip()
    string2 = inputFile.readline().strip()

    distance = editDistance(string1, string2)

    #print str(distance)
    output = open("output.txt", "w")
    output.write(str(distance))

main()