def burrows_wheeler_transform(word):
    '''Performs a Burrows-Wheeler transform on the given word, returing the transform.'''
    # Check that the word ends in the out of alphabet character '$'.
    word += ['', '$'][word[-1] != '$']

    # Store the length of the word to save a marginal amount of time, as we'll call the length often.
    L = len(word)

    # A lambda function to get the nth character of the cyclic rotation (to the right) by i characters.
    cyclic_rot_index = lambda i, n: word[(n-i) % L]

    # A lambda function to compare cyclic rotations without generating the entire rotation.
    # Use the previously defined lambda function to compare rotation indices.
    cyclic_comp = lambda i, j, n=0: [1, -1][cyclic_rot_index(i,n) < cyclic_rot_index(j,n)] if cyclic_rot_index(i,n) != cyclic_rot_index(j,n) else cyclic_comp(i,j,n+1)

    # Sort the cyclic rotations based on their shift using the previously defined comparison function.
    cyclic_sort = sorted(xrange(len(word)), cmp=cyclic_comp)

    # Return the last index of each cyclic rotation in the sorted oreder joined into a string.
    return ''.join([cyclic_rot_index(i,-1) for i in cyclic_sort])


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('input.txt') as input_data:
        word = input_data.read().strip()

    # Get the Burrows-Wheeler Transform.
    bw_transform = burrows_wheeler_transform(word)

    # Print and save the answer.
    print bw_transform
    with open('output.txt', 'w') as output_data:
        output_data.write(bw_transform)

if __name__ == '__main__':
    main()