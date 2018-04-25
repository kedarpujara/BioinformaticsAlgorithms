def graphToGenome(genome):
	list1 = []
	vertices = []
	edges = []
	isTrue = True
	for i in range(len(genome)*2):
		edges.append(0)

	for i in genome:
		edges[i[1]-1] = i[0] - 1
		edges[i[0]-1] = i[1] - 1

	for j in genome:
		begin = j[0]

		if begin in vertices:
			continue
		if begin%2 == 0:
			end = begin-1
		else:
			end = begin+1
			
		P = []
		i = 0
		while(isTrue):
			if begin%2 == 0:
				P.append(begin/2)
			else:
				P.append(-(begin+1)/2)
			dest = edges[begin-1]+1
			i += 1
			vertices.append(dest)
			if dest == end:
				list1.append(P)
				break

			if dest%2 == 0:
				begin = dest - 1
			else:
				begin = dest + 1

	return list1

def main():
	file1 = open('input5.txt')
	pfile1 = file1.readlines()[0]
	pfile1 = pfile1.replace(")(", "),(")
	pfile1 =  pfile1.replace(" ", "")
	P = eval("[%s]" % pfile1)
	text = graphToGenome(P)
	#print text
	f = open('ot3.txt')
	line = f.readline().replace('[', '(').replace(']',')').replace(', ', ' ').replace(') (', ')(').replace('((','(').replace('))',")")
	output = open('output.txt', 'w')
	output.write(line)
	#print line

main()





