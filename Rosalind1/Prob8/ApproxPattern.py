def ApproxPattern(pattern, text, d):
	list3 = [];

	for i in range(0,len(text)-len(pattern)):
		currPattern = text[i:len(pattern)+i]
		print(currPattern)
		if d >= HammingDistance(pattern, currPattern):
			list3.append(str(i));

	print " ".join(list3)
	return " ".join(list3)




def HammingDistance(dna1, dna2):
	list1 = list(dna1)
	list2 = list(dna2)
	count = 0;
	for i in range(0,len(dna1)):
		if list1[i] != list2[i]:
			count = count+1;
	return count;


ApproxPattern("CATTATTATGT","CACACTCGACAGACGCGCCCTCAGGGCTCAGTCCTGCACCGGCATCGTCTTTAACCACGTCTTCAGGGGTTGTAATAAGGCCGTGTTATTGCGTCACGCAGGCCCCCTGGAGTGGTGACTTCGGATAGGTATTAATTCACAGTGTGCGCTAATCTCCTGCCCCGGGTGGAAATTAGTAGAAGACCCAATACGAGCAGACCGCATACAATTCTCTGTTTAAGACACGAGCTCTAGGACATAGTACCGGCAAATTATGTTCCAGGCTGATGAACACGGCGGATAACTCCTAGACTGACGGTACTGTACATGCCCTAGCACGTCGTCTGAAAATTATGTCGTTTAAGTCTGTGTTGGTATATATGGAACGTATCTAGAGGATCGGTTGTGCTGTTAAAAGGTGAGTAAAACCTTACGCTAAATTGTTCTGGTGAAGCACTGTTCAGAGATTGCTGGGCTTAACGGAAGTTAATCTGGCTCGAACCAAGTAGGAAAGGAGACTGCCTGCAATAATTTGGGGCATGTATCATACATTTGTGTTACAACACCGCGGCAAAGTATCCTGCCGAGGCGAGACAAATGTGATAAGTACTCGAAATACTTAAAGCCTAAAGATGGGCCTTCGGCCTCATATGCAGCGCTTCGAAACCCTTTTCGTGACCAGCGGTACCCTTGCCGAGCCATTCATAGGTATGGCTCTTCAGACCCAGAGGGGCGCCAGAACGACGGTCACAACCTTGGAGGCGTGTCTGAGCGTGTCAGCGTCAGCACACCTATAGTTCTCTTGATAAAGCGCCTGGAATCAAAAGTCCCAGGGCGAGCTACTTCGGATTGTCATCTACATTCATCGGTGGCGGTCCGATGACGATCTCCAAAAGAGCTCAACCGTACGTCCACACACATAAAATGTGATTTGTGATGCATTTGCTCTTAGCGTGTATCTACTAACCGCCAGATTTAACCGCCAGCCTTCAGGGACCGCTACGATGATTATCTACTATGTTACCAACGGCGGATCTCAGCATGGGAAAGACAGACTAAGGCCGCCGGCCATCCCCGCCAACTCCAGCTCGCTCTCCGCACGTTTACATAAGAGACGACTTCTATAATACTCTCAGGCTATGACAAAAGGAGAGACAAAACCAAACCAGGAGCAGCGCCTTACTTTAAAAGCTCTTCTTCTGACCGTAGATACGTTTGAGCACTACAACGCTATCGCAGGTGACCAGACTTCGGTGTATCATAGCGTCCCGCCTGGACGGTCTTTATTGCGAACTGCGCGGTTGGCTTTCGCCTCCCTGGTGACCGTCCCACTGCCAGACCCACTCCCGCAGTCTCCGATGATTACTCACCTCGTATTTTGCGCGACGCTCCAAACATGGAGTCAAAATTCCTAGAACTGGATAAGAGCAGGGGAGCAAGAGGCGCGTCTTTGCTTGCAGAGAGTTCCGTTACCCCTCCGCGCATTTCCTTCAAATTAGCCGTCTCTCGCATCGGAAAGGTCTGCCACAACATGGCACAGCTGTTGGGGCCCGTTGCGACGATTTCATTTGTTACAGTCGGGCTCATCTACTGTTTAATTTATACAGAAGAACGGTGGGCGTGCTCCCATAGCAACCCGGCATACATCTTTCCGCTGCCTGCGCCACCGAGTCTATGTGAGCTCTGTTGAAGCCTGCGGCACCCGTTAGTCCTAACTTTGACAGAGGAGTGGGTCCTGCTGTGCTTCTCAATCCGAGGACTCCTATAATCAGCGATTTGTTAATCGTTCCCCAAGCGTCCGTAAGACCGTTTGGGCTCTTTACACCTCGATGCGACGAGCATATGCCCACTTCTTTTCACTCATGCCCACCCAAACCGGTATCCGGAAATCAGTAACACGCATCCAGGAGACCCGCGTATGCAATGAGAGTCTGGTTCATAAACGCGCCTACGTACGGAACGGGGGATTTCTTTTATGCAATAGCTAATTTTACTGCACGGTCTACACCAATGGTGATGGTCTAAATACGACGCCTATTACATCCCATTAAGCGAATGTTTATTCTAGATCAATCGGGACACCTCGGATTTACGATATCGCTAAAGGAGTGCAGACCCAATTCGGACTCATGACGTACCCTAAAGGTCGTTAGCCTTCTGAGACTGGCCGTCCAACTAAGCACGCCACTGGACGCTCCGTAGCCAATTTATGTCTGGAAGTAATAAGGCTCTAATTAGCCTGAGGGTGCCGCGCAGTTCGCCCTGACAGATCCCGAATATTCGGGAATCTCAAGCCTAGCTAATGAGCTGTTTGACTGAGCGCGCACAGGTATATTTCAAATTAGTGTCGTCCACGAGGGAGTCGTATTCCGTCGAATGTTAGAGGCGCCGCACCCGGTTTCGGAAACTTGTGACGCGTGGACTACCAGCTAATTCTCTCGATAGGCGAGAACGCATCGCGATTGGCGAGCCGCGCGAGTGGCCCATGGCTCCCTGTCGTTGTGTCATGGCTATTTCGACTGATGAAGTTAGGGCAAATTCCTCGTTCAATCACGGTAGATACGAATCTCTACTGATTCCCTTCAGATTGGACTGACGTGCGAAACACACTTTGCTGGCTGGACACAAGAATAAACAGCTATCTGTCAACCAAGTCCACCACACAGCCCCTAAGCTCAATTACCCGTCTTAAAATTTACCGTGGTGGCTCAAGGCGCGACACTGTTGCGCGTACTGGCCCGGTGGCATGATTAGTATACCTCAGGGGCTGCGGGTTGTAAGCATAACTCTGGATGCAGGGGTCTTAATTTTTTTCAATAGCCCGGTTAGTGCGTCATTCGCCACTTCCAGTTCTTGTCCACCGACTGGTCCCTGAGCGGGCGATTAGGAATTCCCAGTGGCAAGATGACTATGTCACGCAACGTTGCAGAGCAACTCTTCATTGATAACATACCTTAGAAATGAATTGTCTCGCCTAATTTCTTTTTCATCGAGAATATGTGTGTTGTGGTTTAGGTTTGCTATGAAATTCGTGATATCCCCATTGCGCAGCCCAGTCACATACAAGTGTTGGGAGGAACCGTGACCTTACTCAGGTTGAAGTGACACCTTTATCTTACTATTGCGTTTAGGAGCAGAAAGGTCGCCAACTCAAAGCGCGCGGCTTGAGCCTAGCCGCAAGGAAGCGACCGCGACGTGAGTGCATTCGAACGTGATAACTCCAATAATGCTCGCCCGCGAATAATCTACCTACACTACTCGCACTGTTCGAAGTCTTGTTCTCGTAGCTTGTGATCAAGCGTAAAAACGTGCTCAATTTAGGCTACCTGTACCGCGTCTCGACCTATGAGAATTCGTTGAGTACCAAGTTTATGTAAAAGACCCATTCCTTGCGCCGGGGCTAGCGCGAATTGTCCCACTGACACGACGGTTACGCACATTTCCTATGTCCATGCGTTCAGTCCAAACTTCCACTTTGACCACCCACCACACTCACTAAACACTGGTACACTCCTAATGGCTAAAGCGCCTGATTAAGTGACCAGATGATGTTCACAGAGCGGGTAGTGGAGAAAGGGATTTTCGATCTTTGGCAACCATGCTAACTGCTTAAGCAATGGTTAGGGGTAGACATCTTTTGGCCGTAGCGAATCCCTTTTACGACGCTGGCGCTCTAAGTGACTAACATTTGGATGTCACTAATTTTCCACGTGGCCTGCAGGCACCAATCTCGGCCCCGGCCCAACCCGTCGGCGTGGCTGCACGGTCTTGCATGGACCTCCCCGTATAAGAGAACATCTTCATGTTGCTGACCGCCAACAGGGTCTCATATTTGGCACTAAAACCTTCAAGGTGTAAATGGTTTATCTAGTGCAATCGAGCTCCCCTGTCACCCTTGGCACTCCACGGTCTATACAGCTTCTCACGAGCTATGCTTACACTAGCCACGAACATCCTTAATACCAAATCATGGGTCCAAGCGTCGGAGTTGAAATTAAAGTTGTAATGCTTATAGTGAGCAGTTCGGGATCACCTCGAGGGTATAGATTTCAGCCTGGGGGCTAACAGTCAGGGGGCTCTAATCATGTCCGCGGGCATGCTTAACGCGCGGTGTCATGGCTTAGGGCATGGGTATGAAACGTGGGAAATTGAACCAGAGTACCAACAGCTCCCCTACTTTTAGATGTTTCTTCTTCTGCTACCGGTACCTAGACAATGTAGTGTATTTCGCCACTGAAATGCGTACAGATGGGAATTCCCTGAGATGCTCCGGACCGGGGTAAGTCGCAGCAGTCACGGGCTACCGGACCGCACTAGTTTGTAGTATCGACACCAGGTCAGCCTACACAGGTAAATATCACTCAGCGTTGACTGGATCATTAGTGTTCGGTATGGGATCGTCGAAGGTAGTCTTCCCACGGAAGCGCTCGCCACATGCTCATAGTCTGATACGGTGTAGTAACGCTCCTATATAGTAATTAAAAATTGCTCCAAAGTGAAGACCTCGGTAACGACCCACTGGGCATCTTGAAATCTCCCGGATGATACAATTATCATGCAGGCGCCTCGTCGCAGTCGACTATCATCAGATGCGGGGTCGCCTTGCCAGGGTACCGCAGCTCAGCGCCCGTATACGTATGGACTCTAAATAAGGAATTGTAATCTTTTCAGTAACCGTCTTTATCGACGTGGGGATACTCCATGGCTTTAGCGAGGTCACGATCCGACATTGTTGCGGCTTAACTCCTCCTACTTTGAAGAGCATAAGCGACACATCCTCTCCGGCCAAACCCTAATGGATAGACGACTTTTCGGAGCCAAGGATACCAAGAAGTCGTACAGCTCTGGTTGAGATATAAAAGAGCACATAGGGCGTCTGTGGGGCACTGAAAGGAAAAATGCAAGAAGGACCTTACTCATCGCCCCTGAGTTAGACCCTTAATCGTTGGAATTTCCTTTATAATAGCTACAGGCTGTACAAACTAACGCAAAGGCGAGATGGAACATTGAATCTGAACGCGCAGAGAGCGGCCCATGACTCCACAAGACTGAATCCTGACTCATCAAGTCATCCAGGAACGCCTGAGTATACGAGCGCAACCTACGCCGCCTGATAGAGTAACACCTGAAACCCCCGAAAGTTCCGGCGCTCAGTATGGTCTCGCTCTGGCGATCGCGGAGGCCACTGGAAGACACCCCGGCTGTAGTGGTTACCTCTGAGGATTCCCCGTATTTCGAAACTTCTGGACATTACAATCTGCGCATGTGGCCTGTTTGTGAGGCGCATACCTGTGTCATACTAGACGCTACTGGCCCGTTCGAGCCAATGGGCTAAAACTTGAGATTCTTCTCACGCGTTTGCGCAGATATTGGTTGTTGCCTGGCCCGACGGGTGATACATTCAGCAGATTACCTACACCGTTTCGTGATCAAGCTCTCTCTGCGGAGGTAGTCCCATGATGAATTGTACCGACCCTACAGCTCTGAGACACGGGCAAAGGATAGTTAATCCAAACCTACATGCCAACACGTTGCACTGGATTCCGATAATAGGGAATTCGTGGCCTCTTTTTTTGATATACATACTTGAAAAAGCCAAACTATCTTCTTATTTCGATAGTGACTTCGCCGGCGTGCGTATTACCGGGAAGAATGCTAACAGCTCGGTACCGACCGATACGGTCCGCTCACTTGTCGGGAGGATAAAACATTCGTCACTGGGCTGGTCACGAGATCGGCAGCGTTGTCTTTAACCTCATGCTGAGTGTCCTTGCCTCCCGAGACAGTTCAACGTGCATTATCAAGACTTTACTGGATGAACGTTTAAGGCCAAGACAGTTTTTCGTGCTAATGTGCAATGCGCTCTACGGGAACATACCCCGAGCCCCGGAACTTACCGTACTACACCTCCGAGGCGTCTTGACTTATCGTAATTCAACGCTTTCTGAAGATCGGGCGGGTAGGAACTTTCGACCAGGTCCGTCAGCGCCAAACGACCCGGCTCTCCACGAAAAACGCAGGGGTCGTGCCAAGAATCTCCGATGTAATTGTGATTCTAAAACACGCCCAAAGCTCAAATCTAGTTAGTGCTTACTTGTGCTTTATCATAATACCATAGAGTCGTGCGAGTGACCTGGCGCAGGACCGGGGAGATGGAGAGGGTCACCCGGTGGGTAAGTCGGTGATAAGTTGCGTTGATCTTGCCCGCTGGTTAATACGTTTGATCGACCTCTTTAGTCAACCCGTCGGGGATTACCTTGGCGTTCACCTCGCTGTAGGGACCCCCGTCAGATATTTGCAGCCTATATGATACAGCGCCATTACTAAGCCTCGACCGGGAGTCGTAGGGTGCAGTAACTACTTCAATTTTTCCTGATTTGTCTCGGAATGCCGTTTCTGGGCATGTGGAATAGAGACTCGATGCAGACCTGGGGATTCTGCCGACGCGATTAATATGGTGCCACGGCTACGAGTCGGATTGTAGTCACCTGAATTACCGGATGACATGACGTGTCAATAGCCTGACAGTATGTCAGTACGCACTTGCCTACTAGACCCCGGGAGCGAGGGCCAATGCATGGAAACTCGCTCGCCCAAACTACTTTAGCCCTCGGATGCGAGGGAAGCGAGGAAGCTGTGTTAAGGCGTGACAAGCAACCCCGCGTGATACAAAATGGGGACCACAATCGCCCTCGTAGTATGTTTGATCTGGAAGCGCCATGCTAGCTGTGCTAGGGCCTTTAGACTACTAAGCTACAAGACGTCATCCGAGGAACACACAGCAACCTGGGAAGCGTAGACTGGCAGAGTACGTACTACCAAACAGTTCGAGTCGCGAGCTTCTGCGCCCACAAGAGTAAAGATTACTAATGGATGCGTTACTCCATGGAAGGGAGCTGTATAGTAAACACCGATCTACGAAGGCGAAACGTAGAAACACTAACCGGCCTGTAGTGTAACAATACAACTATAAGACGAGTTGTCATTTGAACAGGTAAGCAATCTTAACGCGCTACAACAGAGTTGTCTCCAGGTCCTAGTGTGATTTACATGGCGTTATCGCTCCCTTGCACGATCGCAGTTATAACTCGACATCGAATCAGCTCGAACTGGTATGGCGTAGCCGGGAGATTAATTTGAATGAACCACAGGTTAGTCTTAGGTGGTAACGCTGATCTCTCGGGACTTCACACAACGAACTTATCCTGAGATGTGGTCAGCAGTGCATCCCCCCCCCACTTCTGCGGCGTAAATTACCAACCGTAAACCGCTGTAAAAGGCAAAGGTTCTTTCTTCCTTCTTTGGGGCGTGTTCTACTACAAAGGGGGTAGAATGGATGCTTTAACTTTTCAATGTGTAATACATTCCGCAGTTTGTCCGAATGAAGTATTGTGCCAGCGTCCTACTACTCTCCACGATCGCACTGCGTAGGGCATCCATCAGCAGGTAATGCTAGGGCTAACGGTTTTTGGCATTTTCTGAAGGCCGCGTATAAGATATAACGGGTCACGGTAGTAGATGCCTGTTGGGTACCAAGAAGCTGCCGCAGGATTCTTCACGATGGCGCGAGCTGGAATGAGGCCAGCCTTATGGCGGCGTAATTATCTCCCGGAGCTTCGCATGAGTAGCAGGTTCAGGTCGTGGACGGATGCCAGACGCTACCCTGACAGTACGGGAACCGGGTCAGGGGGTGGCCAGGGTATTATTGTCTAAAGGGCAAGCGGCGATTGATCGCATCGCGTTACCTGTTCCCTTTTGTTTTGTTGCAACTTTATCTCTAGGTCTTATTGCGATTGCGCAACTTATACCCCCTTACCTTTCTCCTAGCAACCCTATTTAGCTAAACGAGCTCCCCATTCGTTCAACAGCGAGCTGTGGTAAAACGGATATAACTCCAGACTGTTACGAACTTCGGGGTAGGCGCAGGAGGTACCTCGTGTGATTGGAAGTGGGGTACCCCTCGCTGACCGTCATATGTAGTCCGCCATCGAAGGTTCGAGCCTTATAGGTCCCCCAACTTGGGGTCAAACGTTTACTTAAGTCATGAAGACTTTAGCATAGACGGTAGTCAGCAAAGACTCGTGATTGGATCGATACTGGCAAGGAAATTCACATTACCCCATAATGAGGACCGCGTGCTCGGGGACTGTCTACTGTGCTGAGCCCATCTTTTTTGCTTTCTGGTAAGTTGGGCGAGATTAGTCTCGTGCGTACTCCGGGGCTTAGATACCTAGCACGCCGACTCTTACGGTTTTAACACGGCGAAAGTTGGGGGGGAAGCGGTATACCTTCCGCCCGTAGTACGCAATCGAGGATCCTTTCCATTGCTTTACCAACGTTCGAAGGAAACAAGGCGCTGGAGTTTCGTCTTAAAAGATGCAGGAAACAGCCTTTACGAGACTCAAGGCAAACTGAGACTCTCAGGGGCAGATACATTCGGGACAGTAAATATTACAGGGGGGGGAAGACGAAGGTTAGAAAGGTCTAACCATGTGTCTATCTTAGCTCATCCAAACATGTAGGGGAAGCACTCCCAGTTCAACAAGTGATACTATCCGCTGTCGGCCCGTGGACTTTTAGCACACAAATCTGGGATGGTACTGCGGCTTTACTACTGGAGTCTCCATACGGGGACGGAGCGACTACTTGTCTATCCCTGCGAAATTAGAACTTTAGCGGAACTCTTACGGAGAACGGCACTTGTGCAGTTTACGTGGGCCTGAGAAATCCGGACGTAGGACCTATACCCAACGTCAGCCTCAGTCAACATCGGTACGGAACACCAAAGAATATGAAGTGCCATGCTAGGAATAGCTCGCGTACCACCTTATGTTATCCTAAATTGTTTTACCCGCTTGCTTACCCTCAAGAGCTTGAGTGGCCTCCGTGGCCATACTTATTCCGCTATGAAATGGGTCATAAGATCCGCGCATTAGCATTTTGTAGGTTAACACAAGTACGTGGAACGCGGCAGTGGGATCACCATTTTTCCGACGGCGGAGGCAAATCTGGTGCAGATGGTCGTCCTGAAGTGGTTATTATAGCGCTCGCGTACACCCTCAAACCTTATTCGCAGGTTCGATCACTTGTGAAACTCCGTGTTACCTGAGCAGATAAAGGAAACTTTAAAACTCTGACCTACCAACGACCTCCTCGGCGTCCGCCGAAGGCCGAGGGGATTGAGCAGAGAGAATGTTGGCAGCGAAGTTCACGACGTGTAAGGTCAATAATATTGAGAGCACAGACTCTTACCGTTGTTGCATGCTGTGATCTTCTCCCCGGTATGAGATCTAGTAGTTTATGAGACATCTCCGCCAACAAAGTCCTCAGGATTGACCTCCTTGAGGCGACGGATGTCCCACTACCGAGTACTCGCACGACTAACATCCTTTGGACCAGAGAGCTCTACATAGAAAAGGGCGGGTCCCTCACTCAGGTGACCGTGGGGCTCATTTCCAACGGGTGCACGTGTAGATTACTTAACTTAACGGAAAGGCAGAACTCTGGGGTATCCTTCTATATTTGATATGAAAGTCGGGGTTACACTACGGCGCGCTCTAATAGAGGAGATGCATGGCTAGCGTCCATACTACTTCTCTTTTTGATGCTAGCGACCTCCTCTGGTAAGCGCACTACCGGACTGACTATTAATGTAAGAAATGCCTCCTAAATGCTGCACACGGCCCTACGAAGTATGGCCCCAATCGGATACGCAACGTCATCGTACGTCGAGTGTTGTAGGACTACCGCGAAGTTATGCGTCGTCACTGAAGCCGATGCGAGAGCTTCTGCATAGTAGGATAGGGTGCCATTACAACATTTCAGGGTGGGCAACCCCGGCTGAATCAACGAGCCGAAGCGACATGGCAACACATCCAGGGAGCTATCCAATTATCTATCGTCCTCTTAACTGTCTCCAATGGTGGCCTACCCCCAAATCGTACTCTCAATACGTTACGGAGACTGGGAATTTTAGCTTTAGCAACTTGCTCGCAAGGGTTCTATGCAGCGCTATAACCTCGTTGTTTTGGGAGGGAGCTGCCCTGGACCAGTCGCAGTTCGCGCGATATTCCCCTTCGTGAGACCAGTGGCATTCACTTAGGGGATGAACTGAGCCAATAATTTACATGCGAATATCCGCTTCGTATCTATTCTCGGGGTGAGTTTCAGACTCCCTACCGTACGCCCCATCTGAGGGGCCGCCACGTAACGTTCTATTGTCCTCCCCCAAGGCTTCAAGAGGAAGTCAGCTATGGACTGTGGTGTAGCGTCTGTATTGAAGATGACTTACGACACTTCCAGTTCAGTCAGTTGAATTCCGTAGCAGCAAGAATTTAGACAAATCTCCTAAGGGTGCGGTTTTTGCACCGGTCGCGGGGGCAACTTAGCACCTGGGTACCCAAATTTACCTACCGGACTCGGTAACTAAACAGTAGCGCGCTTGAGAAATGGTCGGTGTCGAGCTGGGTTTAAACCCACCCGATACTTTCTACTTCAAGATAACTTATGTTCGAAAAACAGGGTATCTCTCAGCAGGTACTCTCGCGAAGGTCACTCGTATCGTGGTGTGGCTAAATCGGGTACAATGTACCCCAGAACGGACGCCCAAACGCTCTTGTGCATATGACGGTGACACCCTCCAACCGCGCGATTACCGAGACCGAAGAATTATCCAAAGTGGTCGACTGTCATATATTTCGTAGGACTACCTAAGGACGTGTTGCTGTGGTGCCCCCCCTCGAGAAATCTGATAGACCAGACAGTATGGTTCCTCTCATGCAATGGATAGATGTGTTTCTCGTTATATCCGCGAAGATGGAGCAGTGCCTACGCTTTCCCCGTCATCATAAAGCCACTACACGAGTAAATCGTTCAAGTCACGGCGCCGTGGCTGTTCACTACCCGATGATGAAGCTTCTAAGACATAAAGAATACTAAGCCGTTGTCCTGAGCTATCTGATGATACTTCGCCCAGTGCCACGAAATGCCGTGACGCGCGATGGGAAGCAAGGAACTGAGCGAGGTGTTACTGACAGAGGTGCGATGTTGCGATGGATAGGCATAAATGTCTCAATGGTCGAACAAAAATGCCATAGGGCAACCAGGCGTGAGGGTTGATAGCTTTTAAAGCACTATTGTCACTCTTTCGGAACCGGGTCTTTTGCGACTCCCAATGCCCATTCGGATTTCAGACTGTACACTAAGCTAGAGTAACAGCGCCTAGTATACCCACAGGGGTGTGCTCACCCCGCTTGTGTGGTCGGTGTTAGGCACCAGGTGCGGTCCAAACAGTACTTGTACCGTATTCTCCAGGATTTTTCCTGATTCTAGGTAGCTCTTCCTAGAGCCACCCCTGAAAACTCATAGTCAAGCGGAACCGTGGTACGTGAGTGCGAGTGTCGTTCACCAGTGACACAGCGCACATTGGACGCAGTCAGCCTGAGCCCAACTAATGCCCTTGTATCATAAGTGCATGATGGTTGGTGAGGAAGCAATGTCTACGGCTTTGTATGATTCTGGAGGGCATCGACCAAAATTAGATCATGCAGGGCAATGCTCTGTGCACCTCCGGGTACAGGTAACCTTTAGCCCCAGGACGCTACCATTGTGGACCCGAAGGTCCGCATTGATGTCGGAGGCCCGAAAGGGGTATCAACAATATGTCAGAGTGCCCATCGAAGTAATACCGTCATCAGGGCCGCGAATGCCGGTGCCTCGTTCCTCCTCGCGAGTGCGCAACGTTGTATTAGGGTGCACAGGACTCTGGATAGCACTCTAGAGCAGATTAATCGGTGCAATAGTAGATGTGCTAGGAGAATTCTGCATTATAGGGGTTTAATCTTGTCTAGCTGGAAACAGCTCTTAAGGTGACATTGTTTACGAAATACTCCCTGTAATACTCCGCGCTGCGAATTGTTAATGAAATATACTAAGCACATCGGACGAGTAAACGAATGTTACGTCTGACCGTTGTTTGCACCCGTAAGTCGTTGTACGACGGCGCTTACGGAATGAGCATATCCGTGCAGGCTTATTAGACGCTCATTGTGGGGCTCGGGAGTGGGAGGTTGCAGGACGAGACTTCTTCTAACTGAAGACGTAAAAAAGGTGCGGAAGTTTATCTGTGGTTAGCTTTAAGGCTCAAACCATGAATACTAGAGGGCCTGCTCGTTAAAATCCAAGCAAACCCAATTAGACAAAGTTATTATAGTCCGCTAGCTCTATCGTGGCTCTGGAAAAGTGTCAGTACTCCTTCCTTGGGAGCTGTGCTTTACTCCATGCAGAGGGGTCGCCCGCACAAGGCTTGTGGTTCCGGGTCTGTAATCTGCTGACGCACCGGTCTTTGGGTTACTAAGGCGGAATTGTATACGCATAGATTAGGAGTTTCGCGACGCCAAACCCGCAGAGCCGTCATTCTTGAGGAGTACCCAATCACAGCAACCCGGGTTAGGTACTACCGTGTCACCTACCATATAAATTGTTAATAGGCGTCTACGGCTTGAGCAAGTTTTCTCAGCGCATGGTCTGGACAAAACAGGTTGTGTTAGCTTTGATCTGAAGATAGGCATAGGTAAGCAGTTTCGTGTACCCTTATAAGGTGATGTGGTCCCTATACATTAAGTAGTCCCAGAGTCACGGGCTGGTGGCGACACCGTACTGGGTCGCCTCGAGATCATACCCTGCCACGCTGGCTGCAACCGGCCGCTGCCCTAGCCGGCGTGCACTGGGATTTCGCTGGCAGGGTGCCTTCACAGGTTTCCGTGCTAATGTTCATATGTTCATTAACCTCATATGTGAGCAGTGGCGCATGGCCTGCCACTCTGCTCGTTAAATGCAGAGACGTAAGCTGATGTCATGGGATTGTCTGACATAGGAGAGGGACAGGGCGCCCTTGAAGTGGTACGGCCGTGGAGCCGTCTATCTCACTACACATTAGAGTTGCCTATGCGAGCAAGTTGGACGGTCCGCAAAGAAGGCCTACAGTTTGTAGGGCGCAGTGACAAGCCCAGAGTACGTCGTGTCTTGAGTATAAAGGCGTATAAGGTATATATGTCCCGCTGCGCCAGCCTCGCACACGTATATTACCTGTGTATTCTGACAGGCCGCATAATCTGTCGCTAGTTTTCCGGCTCCTGCTAACCATAACAGGTTGGAAAAGGAAAACGGACACCCCTAGTGCGAAGCTACCAGTGACCTCTACTAGGTTGCCGAACCCACATATAAGGGGCGACTGTGTCGTCAATGGAAGCGCGTTGTCGAAGGACTTGCTACGTCGAACACCCCCCGACGGAGGGTCAGGGAATAGATCGAACTTCGGATATATGTTTCTTCAGTATCGCCGGGGGCTTTTCTGCAACACGCCTCGGCGCCGGTCTCCTGTAGTCAGATACTTACCATGCCAGAGACTCTTACAGACCTTCCCTGGTGCCAGTGAGCATATAGGGGATTCATCATCTTTTCTGTTGCCCCCCGTGATTGCCCATCCTAATGACGATATTTTCGTCTGTTGAGGTCTGCACTAGAGCTTAGAGCAACGCGTATGACCGGTACTGGTAGGTGAAATGGAGACAGTCGCAAACCGGTTAGTCTATATCAGCGGAGGGGACTGTTACAGAGGCTGTCTCAAGTTAGGGCTAATCGTAATGATATCAAGGACTTAGGGGCCCGGCGTGGGTGTTCCTCGGAGTGTAGAACAGGTATTGCGCCAAAACACGTGACCTAGGACCGATGCTGCAATTTCGGTCGGCGTCTATTCCTGTGCCGAGAGAACTCTGCCGCTTGACAGGGCACGAGGGAGATACTGAGGGACTTGCGCCAAGCACACGCGTAGTGAATGGTTCAGCCAATATGCGTTGCACAGCGCTTACGACTTCCGTTTCTGCTATCAATTCCAGACGAGTGACCATAGTACACACGCATCCCATGGGCTGCGCGTGTTCAGGGTCGGGTAATTGAAGGTACCGGGTTGTTCTGACAAGTGACAACCGGCTCTCTTCTTAAGATGTGAATACCCATAGTTCATAGTACTAGGGATCAGTTGAAAAGAGGGTTTGTACGCGGTCCCAGGCTGATAGCCGCACTTAACCTTCCCATGTCCGAGATGAGATATGCCTCACCTCGTATGTCATGGGGTCGCTATAGTGCATAAGCTGTATAGCACCTAGGACGTAAGTGTCCTCTGCGGCGCTTGTGTGGTACATGTTATTACTCAAGTCACTGCTGATTGAATTTCACCTACGGTGAAGGTTGTGCGGCTCACTAATCGCGAACACTACCCGGCCTTATGTGTACACGGTGGTATGGATTCAAGCTGTTGCGTAATTCGCCTCTGGCGAATTTACGAATCACACGGTGTCCTTTTCTCCTGCTAGATTGGGGGCTGTGAGTGTTTGAAAGCTACAAGGTTGGGATGCATCTTAGCAATTACGGTCTGTTTTTCTTTCGGAAGTGAGCCAATCATGGAGCAAAGGATTCGACACACGCGTATCAGCGCCGGAACGGGGGGGTCCAGGCTAAATGGTAGTAGGCGGAGCTGATACTCGCCGGGTAGTCCTATCAAGCGGCATGACGTTGAGTGTCCAGGCTGAGGACCAGATTAATGACGGGTTTTAGTGTAACACACTATCCGCTATATGACCTTGAGGTTGCCACGGGGCCTGAGCCTACATGTCCAGTCTCATCTAGTCACCAGCTTCCGATTACTAAAATCAAACAACAGCCTCGTTCCCAAGCACGTCATACCGTGGATTGAGTGAGCCAGCCTCCACTTTTAGTACTCAGGGGACACGGTAGGGGTAAAGCGGTCTTAACCTTCGCAACTAACAACATGGTTATGGACTTAGTTCGCCGTATCACCCCCCAGGCTCCTATCTCGGGTCGGTACTACCGCTACGCGGGCCTCGGGACATTTAGTTTTATTGCACCTTATGGTGGGTAAATTTTCGTAGAATTATGTGCACAATACTCACCAACCATAACCATAAGATTAAGCATCGTAACTGCAATGGCACATGCAATGTAGAAATTGTCCCCGAGGAACCAGGGGAGGGCCGTGCTGCACGGATCAGACGGCAGAGAACGACACAGATTGGAGTAGTTAGGAGTCCACTCTGTCCTTGGGGAACAGTGTTTCATAGATTACCAGTAAAGCTGGTCATCACACGGTCACTTGTCGACTAACGTCAACTGAACATCTGAGAGGAGGGTTCAGGCACTTAATTCAAGCTGCGGTGTACCGGAGAATCTTAGGTAATTTAACTTGCCGGAGGACGCAAACCGGGTGTCCGCACGAACGCCTCCCCGGATGGTCAGCCGGGTTTGCGAGTCTATTTTATCCCGAAGTATTAAATCACCTACAATTCCAACAATGCAAAAGAATGATGGCTGACTGTAGCATCATACTATGAGGTAGGTGGACTGATTGGAAGGAAGCGGTGTGACATGTCTGTTCTCTGAATTCCTACCCAATTCTGCGAAAAAGTCCTTCGCTCCGATGACAGCACGGAGTGACACCCGAGCAACGTTTGGATTCTCGCAAGCGAGCTAGGATAATAGGGATCGAAGTTGGTAATGTCACGATGATCATCTTGTTAGTATGGCGATTCTTGGAGCCCGCACAGCCAGATGCGTCCGTTGTGCGCGGCTTATGACCATGCCAACCTACTAAGATCGGCCATAGGCCAAGACCTTACTCGATCTCTTGGCCATCCGGATATTAGATCAGACCAGGTACCCTTAGTTTATGTTGAGAGCGGCTACTACTCTAAAAGAAATATAAGCACTACTAACGAAGCTATACTACTTATTTCTTGTCTCGGCTACATGTGGTGATAATTAGGACTGCTCTTTTGCATTCAAGATTATATGACGAGGTGTTTTGCCAATGAGGACATTTAGACCCCGATCAGGACAGAGGAGGTTTTTTATGCGCTCTTTCGGTGTAACTCCATCACCCAAACTTCTTTCTCCGCGCAGGGCTATGGCTTCATCTAAAATTTGATACTGCCCGCTCCGGGGCTCTTTAAACTAGCCGTAGTCCGTGGCGTCGCTCATCGCTCTAGCAGATCCGTACATCGACTAGTTCTCATTAGGCAAATTCCGTCCTGCCCGATGAAATTGACTGATTTCCCCTGGGACATTCGGCGTAGACCAAAGATATTAGTCGCACTCAACTACCAATTTATCTGCCTGTCCGTCAGGTGCGCGAGTGTGTCATGTGTAAACTCATGCATGGTTATCTAGGATTCAGGACGCACGACACGTAGGAGTATAGATACAAACTATGTAGTGGGGACAGAAGGGATTTCGTGCTGAGCGTAATGGGTTAGAGGCCCCAGTCCGAGAAGTCACACGCATTTTACTCTGGTTTCATCTGTAGAAATGAATCCTAGGACACACAAGAAGCTTGTGTCTTCCGGATCGATTACGCGAGGGGCAGATCGCAATGTTATCTGCCTGAGAAAGACTAATCTCTGTGTATGTCACCGAGAAGTTTAACTCTAGCTATGCTATCTGCTAACTTGGGAACCGCTGTGACCTTAGGTGTCTGGTTCAGATCGGGTGTTCTCTTGCTACCCTGCGTCCGAGCTGTACGGCTGTGAATGACAAGCCCACTCCTCCGATGTCGTCGGACACTTACAGTGTATAACGCGTTGAGATTGATGCTTTCGATATCGCCAGAAGACGTGTATCCGTCCGTTCTGCCCACCGAAAACACGAAACCTCCCACCTAGTCTAGGCTGGTACACAATAGCAAGGAGCTGTAAATCAGAAAGCACAACTATGAAGAAATCCACTCCCCTCCATCGATTGCGGAGATATCATACCGCATCAGGAAGGGGAATGATTTTTGCGGCGCGCTCTCTCCCAGTATTATGTCCCCTACAGTGGTGTCGGATAGCCGTCCGTGCATGTGAGGGCGTAGACAAGGAATTCGCCACTTACATGTCGGT",4)