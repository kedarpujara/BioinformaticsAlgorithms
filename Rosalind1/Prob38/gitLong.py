def longest_common_subsequence(v, w):
    '''Returns the longest longest common subsequence of strings v and w.'''
    # Initialize the array S and iterate through all character of v and w.
    S = [[0]*(len(w)+1) for _ in xrange(len(v)+1)]
    for i in xrange(len(v)):
        for j in xrange(len(w)):
            if v[i] == w[j]:
                S[i+1][j+1] = S[i][j]+1
            else:
                S[i+1][j+1] = max(S[i+1][j],S[i][j+1])

    # Recover a maximum substring.
    longest_sseq = ''
    i,j = len(v), len(w)
    while i*j != 0:
        if S[i][j] == S[i-1][j]:
            i -= 1
        elif S[i][j] == S[i][j-1]:
            j -= 1
        else:
            longest_sseq = v[i-1] + longest_sseq
            i -= 1
            j -= 1

    return longest_sseq


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('input4.txt') as input_data:
        dna1, dna2 = [line.strip() for line in input_data.readlines()]

    # Get the longest common subsequence.
    longest_subseq = longest_common_subsequence(dna1, dna2)

    # Print and save the answer.
    print longest_subseq
    with open('output.txt', 'w') as output_data:
        output_data.write(longest_subseq)

if __name__ == '__main__':
    main()