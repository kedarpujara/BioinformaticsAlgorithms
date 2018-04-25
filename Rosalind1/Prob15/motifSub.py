def MotifEnumeration(DNA, k, d):
  Patterns = []
  for string in DNA:
    for i in range(len(string)- k + 1):
      Pattern = string[i:i+k]
      dpattern = Neighbors(Pattern, d)
      for kmer in dpattern:
        for s in DNA:
          found = False
          for j in range(len(s)- k + 1):
            spattern = s[j:j+k]
            npattern = Neighbors(spattern, d)
            if kmer in npattern:
              found = True
              break
          if found == False:
            break
        if found:
          Patterns.append(kmer)
  Patterns = list(set(Patterns))
  print (" ".join(Patterns))
  return Patterns

def Neighbors(Pattern, d):
  if d == 0:
    return [Pattern]
  if len(Pattern) == 1:
    return ['A', 'C', 'G', 'T']
  Neighborhood = []
  SuffixNeighborhood = Neighbors(Pattern[1:], d)
  for Text in SuffixNeighborhood:
    if HammingDistance(Pattern[1:], Text) < d:
      for nucleotide in ['A', 'C', 'G', 'T']:
        Neighborhood.append(nucleotide + Text)
    else:
      Neighborhood.append(Pattern[0] + Text)
  return Neighborhood

def HammingDistance(Pattern, Text):
  count = 0
  for i in range(len(Pattern)):
    if Pattern[i] != Text[i]:
      count += 1
  return count

f = open("input3.txt", 'r')
k,d = map(int, f.readline().split(" "))
DNA = []
for line in f:
  DNA.append(line.strip())
Patterns = sorted(MotifEnumeration(DNA, k, d))
o = open("output.txt", 'w')
o.write((" ").join(Patterns))