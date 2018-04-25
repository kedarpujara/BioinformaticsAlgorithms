def longestSubstring(text1, text2):
	len1 = len(text1)
	len2 = len(text2)
	LCS = [[0 for y in range(len2)] for x in range(len1)]

	for i in range(0,len1):
		lcs[0][i] = 0

	for j in range(0,len2):
		lcs[j][0] = 0 

	


def main():
	inputFile = open('input.txt')	
	text1 = inputFile.readline().strip()
	text2 = inputFile.readline().strip()

	strings = longestSubstring(text1,text2)
	
	

main()