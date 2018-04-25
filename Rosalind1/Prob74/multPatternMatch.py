f = open("input2.txt", "r")
text = f.readline().strip() + "$"
Patterns = []
for line in f:
	Patterns.append(line.strip())
suffixes = sorted([(text[i:],i) for i in range(len(text))])
partialArray = []
for i in range(len(text)):
	if suffixes[i][1]%5 == 0:
		partialArray.append((i,suffixes[i][1]))
BW = [cycle[-1] for cycle in sorted([text[i:]+text[:i] for i in range(len(text))])]
count = {}
for letter in set(list(text)):
	for i in range(0, len(text)+1, 5):
		if i not in count:
			count[i] = [(letter, BW[:i].count(letter))]
		else:
			count[i].append((letter, BW[:i].count(letter)))
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

def BWMatching(Pattern):
	top = 0
	bottom = len(BW) - 1
	while top <= bottom:
		if Pattern:
			symbol = Pattern[-1]
			Pattern = Pattern[:-1]
			if symbol in [a[0] for a in BW[top:bottom+1]]:
				top = firstPosition[symbol] + counts(top, symbol)
				bottom = firstPosition[symbol] + counts(bottom+1, symbol) -1
			else:
				return 0
		else:
			return (top,bottom)

def counts(index, symbol):
	for letter in count[index - index%5]:
		if letter[0] == symbol:
			curr = letter[1]
	for i in range(index-index%5, index):
		if BW[i][0] == symbol:
			curr+=1
	return curr

def reconstruct(index):
	count = 0
	while True:
		for a in partialArray:
			if a[0] == index:
				return a[1] + count
		curr = BW[index]
		index = first.index(curr)
		count +=1

answers = []
for Pattern in Patterns:
	if BWMatching(Pattern) != 0:
		top, bottom = BWMatching(Pattern)
		for i in range(top, bottom+1):
			answers.append(str(reconstruct(i)))
out = open("output.txt", "w")
#out.write((" ").join(map(str,sorted(answers))))
out.write((" ").join(sorted(answers)))