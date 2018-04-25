f = open("input.txt", "r")
text = f.readline().strip() + "$"
BW = [cycle[-1] for cycle in sorted([text[i:]+text[:i] for i in range(len(text))])]
Patterns = []
for line in f:
	Patterns.append(line.strip())
location = {}
firstPosition = {}
for i in range(len(BW)):
	if BW[i] not in location:
		location[BW[i]] = 1
		BW[i] = (BW[i], 1)
	else:
		location[BW[i]] += 1
		BW[i] = (BW[i], location[BW[i]])
first = sorted(BW)
for i in range(len(first)):
	if first[i][0] not in firstPosition:
		firstPosition[first[i][0]] = i
out = open("output.txt", "w")

def BWMatching(Pattern):
	top = 0
	bottom = len(BW) - 1
	while top <= bottom:
		if Pattern:
			symbol = Pattern[-1]
			Pattern = Pattern[:-1]
			if symbol in [a[0] for a in BW[top:bottom+1]]:
				print([a[0] for a in BW[:top]].count(symbol))
				print("top: " + str(top))
				top = firstPosition[symbol] + [a[0] for a in BW[:top]].count(symbol)
				bottom = firstPosition[symbol] + [a[0] for a in BW[:bottom+1]].count(symbol) - 1
				print("top: " + str(top))
				print("bottom: " + str(bottom))
			else:
				return 0
		else:
			return bottom - top +1


for Pattern in Patterns:
	print(Pattern)
	print(BWMatching(Pattern))


# def betterBWMatching(text, bwt, patterns):
# 	visited = {}
# 	curr = {}
# 	for i in range(len(bwt)):
# 		if bwt[i] not in visited:
# 			visited[i] = 1
# 			bwt[i] = (bwt[i], 1)
# 		else:
# 			visited[bwt[i]] += 1
# 			bwt[i] = (bwt[i], visited[bwt[i]])
# 	sortedBWT = sorted(bwt)
# 	for i in range(len(sortedBWT)):
# 		if sortedBWT[i][0] not in curr:
# 			curr[sortedBWT[i][0]] = i
# 	top = 0
# 	bottom = len(bwt) - 1
# 	while top <= bottom:
# 		if patterns:
# 			symbol = patterns[-1]
# 			patterns = patterns[:-1]
# 			if symbol in [x[0] for x in bwt[top:bottom+1]]:				
# 				top = curr[symbol] + [x[0] for x in bwt[:top]].count(symbol)
# 				bottom = curr[symbol] + [x[0] for x in bwt[:bottom+1]].count(symbol) - 1
# 			else:
# 				return 0
# 		else:
# 			return bottom - top +1

# def main():
# 	inputFile = open('input.txt')
# 	text = inputFile.readline().strip() + "$"
# 	bwt = [cycle[-1] for cycle in sorted([text[i:]+text[:i] for i in range(len(text))])]
# 	patterns = []
# 	for line in inputFile:
# 		patterns.append(line.strip())	

# 	bwMatch = [str(betterBWMatching(text, bwt, pattern)) for pattern in patterns]

# 	output = open('output.txt','w')
# 	output.write((' ').join(bwMatch))

# main()





