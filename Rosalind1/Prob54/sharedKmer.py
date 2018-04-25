from collections import defaultdict
from string import maketrans

def reverseComplement(dna):
    trans = maketrans('ATCG', 'TAGC')
    print(dna.translate(trans)[::-1])
    return dna.translate(trans)[::-1]

def sharedKmers(k, dna1, dna2):
    dict1 = defaultdict(list)
    for i in range(len(dna1)-k+1):
        dict1[dna1[i:i+k]].append(i)

    return {(i,j) for j in range(len(dna2)-k+1) for i in dict1[dna2[j:j+k]] + dict1[reverseComplement(dna2[j:j+k])]}


def main():
    with open('input2.txt') as input_data:
        k = int(input_data.readline().strip())
        dna1, dna2 = [line.strip() for line in input_data.readlines()]

    sharedKmer = map(str, sorted(sharedKmers(k, dna1, dna2)))

    output = open('output.txt', 'w')
    output.write('\n'.join(sharedKmer))

main()