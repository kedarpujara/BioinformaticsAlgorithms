def middleEdgeLinearSpace(string1, string2, scoringMatrix, indel):
	dist = 








def middle_edge(v, w, scoring_matrix, sigma):
    '''Returns the middle edge in the alignment graph of v and w.'''

    # Get the score of the middle column from the source to the middle.  The backtrack matrix is unnecessary here.
    source_to_middle = middle_column_score(v, w, scoring_matrix, sigma)[0]

    # Get the score of the middle column from the middle to sink.  Reverse the order as the computations are done in the opposite orientation.
    middle_to_sink, backtrack = map(lambda l: l[::-1], middle_column_score(v[::-1], w[::-1]+['', '$'][len(w) % 2 == 1 and len(w) > 1], scoring_matrix, sigma))

    # Get the componentwise sum of the middle column scores.
    scores = map(sum, zip(source_to_middle, middle_to_sink))

    # Get the position of the maximum score and the next node.
    max_middle = max(xrange(len(scores)), key=lambda i: scores[i])

    if max_middle == len(scores) - 1:
        next_node = (max_middle, len(w)/2 + 1)
    else:
        next_node = [(max_middle + 1, len(w)/2 + 1), (max_middle, len(w)/2 + 1), (max_middle + 1, len(w)/2),][backtrack[max_middle]]

    return (max_middle, len(w)/2), next_node





def scoringMatrix():
	lines = open('scoringMatrix.txt').read().splitlines()
	index = {letter: ind for ind, letter in enumerate(lines[0].split())}
	PAM = list(map(lambda x: list(map(int, x.split()[1:])), lines[1:]))
	return PAM



def main():
	score = scoringMatrix()
	print score[0][2]


main()