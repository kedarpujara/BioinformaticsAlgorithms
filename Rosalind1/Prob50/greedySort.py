from operator import neg

def greedySorting(P):
    permSeq = []

    kInd = lambda perm, k: map(abs, perm).index(k)

    kSort = lambda perm, i, j: perm[:i] + map(neg, perm[i:j+1][::-1]) + perm[j+1:]

    i = 0
    while i < len(P):
        if P[i] == i+1:
            i += 1
        else:
            P = kSort(P, i, kInd(P, i+1))
            permSeq.append(P)

    return permSeq


def main():
    inputFile = open('input2.txt','r')
    perm = map(int, inputFile.read().strip().lstrip('(').rstrip(')').split())

    greedySort = greedySorting(perm)
    greedySort = ['('+' '.join([['', '+'][value > 0] + str(value) for value in perm])+')' for perm in greedySort]

    output = open('output.txt','w') 
    output.write('\n'.join(greedySort))

main()