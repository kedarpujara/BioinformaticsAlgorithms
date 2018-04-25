def numBreakpoints(P):
    return sum(map(lambda p1,p2: p1 - p2 != 1, P+[len(P)+1], [0]+P))

def main():
    inputFile = open('input2.txt')
    perm = map(int, inputFile.read().strip().lstrip('(').rstrip(')').split())

    breakpoints = numBreakpoints(perm)
    
    output = open('output.txt', 'w')
    output.write(str(breakpoints))

main()