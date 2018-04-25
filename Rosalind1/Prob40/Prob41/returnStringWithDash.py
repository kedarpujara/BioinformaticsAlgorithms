import numpy as np
import tabulate as tb
def wagner(string1, string2):
	n = len(string1) + 1
	m = len(string2) + 1

	D = np.zeros(shape=(n,m), dtype=np.int)
	D[:,0] = range(n)
	D[0,:] = range(m)

	B = np.zeros(shape=(n, m), dtype=[("del", 'b'), 
                                      ("sub", 'b'),
                                      ("ins", 'b')])
	B[1:,0] = (1, 0, 0) 
	B[0,1:] = (0, 0, 1)
	for i, l_1 in enumerate(string1, start=1):
		for j, l_2 in enumerate(string2, start=1):
			deletion = D[i-1,j] + 1
			insertion = D[i, j-1] + 1
			substitution = D[i-1,j-1] + (0 if l_1==l_2 else 2)
 
			mo = np.min([deletion, insertion, substitution])
 
			B[i,j] = (deletion==mo, substitution==mo, insertion==mo)
			D[i,j] = mo
	#print D, B
	return D, B


def naive_backtrace(B_matrix):
	i, j = B_matrix.shape[0]-1, B_matrix.shape[1]-1
	backtrace_idxs = [(i, j)]
 
	while (i, j) != (0, 0):
		if B_matrix[i,j][1]:
			i, j = i-1, j-1
		elif B_matrix[i,j][0]:
			i, j = i-1, j
		elif B_matrix[i,j][2]:
			i, j = i, j-1
		backtrace_idxs.append((i,j))
	#print backtrace_idxs
	return backtrace_idxs


def align(word_1, word_2, bt):
 
    aligned_word_1 = []
    aligned_word_2 = []
    operations = []
 
    backtrace = bt[::-1]  # make it a forward trace
 
    for k in range(len(backtrace) - 1): 
        i_0, j_0 = backtrace[k]
        i_1, j_1 = backtrace[k+1]
 
        w_1_letter = None
        w_2_letter = None
        op = None
 
        if i_1 > i_0 and j_1 > j_0:  # either substitution or no-op
            if word_1[i_0] == word_2[j_0]:  # no-op, same symbol
                w_1_letter = word_1[i_0]
                w_2_letter = word_2[j_0]
                op = " "
            else:  # cost increased: substitution
                w_1_letter = word_1[i_0]
                w_2_letter = word_2[j_0]
                op = "s"
        elif i_0 == i_1:  # insertion
            w_1_letter = " "
            w_2_letter = word_2[j_0]
            op = "i"
        else: #  j_0 == j_1,  deletion
            w_1_letter = word_1[i_0]
            w_2_letter = " "
            op = "d"
 
        aligned_word_1.append(w_1_letter)
        aligned_word_2.append(w_2_letter)
        operations.append(op)
    return aligned_word_1, aligned_word_2

def align(word_1, word_2, bt):
 
    aligned_word_1 = []
    aligned_word_2 = []
    operations = []
 
    backtrace = bt[::-1]  # make it a forward trace
 
    for k in range(len(backtrace) - 1): 
        i_0, j_0 = backtrace[k]
        i_1, j_1 = backtrace[k+1]
 
        w_1_letter = None
        w_2_letter = None
        op = None
 
        if i_1 > i_0 and j_1 > j_0:  # either substitution or no-op
            if word_1[i_0] == word_2[j_0]:  # no-op, same symbol
                w_1_letter = word_1[i_0]
                w_2_letter = word_2[j_0]
                op = " "
            else:  # cost increased: substitution
                w_1_letter = word_1[i_0]
                w_2_letter = word_2[j_0]
                op = "s"
        elif i_0 == i_1:  # insertion
            w_1_letter = " "
            w_2_letter = word_2[j_0]
            op = "i"
        else: #  j_0 == j_1,  deletion
            w_1_letter = word_1[i_0]
            w_2_letter = " "
            op = "d"
 
        aligned_word_1.append(w_1_letter)
        aligned_word_2.append(w_2_letter)
        operations.append(op)
    return aligned_word_1, aligned_word_2

def returnTwoStrings():

    #word_1 = "ILYPRQSMICMSFCFWDMWKKDVPVVLMMFLERRQMQSVFSWLVTVKTDCGKGIYNHRKYLGLPTMTAGDWHWIKKQNDPHEWFQGRLETAWLHSTFLYWKYFECDAVKVCMDTFGLFGHCDWDQQIHTCTHENEPAIAFLDLYCRHSPMCDKLYPVWDMACQTCHFHHSWFCRNQEMWMKGDVDDWQWGYHYHTINSAQCNQWFKEICKDMGWDSVFPPRHNCQRHKKCMPALYAGIWMATDHACTFMVRLIYTENIAEWHQVYCYRSMNMFTCGNVCLRCKSWIFVKNYMMAPVVNDPMIEAFYKRCCILGKAWYDMWGICPVERKSHWEIYAKDLLSFESCCSQKKQNCYTDNWGLEYRLFFQSIQMNTDPHYCQTHVCWISAMFPIYSPFYTSGPKEFYMWLQARIDQNMHGHANHYVTSGNWDSVYTPEKRAGVFPVVVPVWYPPQMCNDYIKLTYECERFHVEGTFGCNRWDLGCRRYIIFQCPYCDTMKICYVDQWRSIKEGQFRMSGYPNHGYWFVHDDHTNEWCNQPVLAKFVRSKIVAICKKSQTVFHYAYTPGYNATWPQTNVCERMYGPHDNLLNNQQNVTFWWKMVPNCGMQILISCHNKMKWPTSHYVFMRLKCMHVLMQMEYLDHFTGPGEGDFCRNMQPYMHQDLHWEGSMRAILEYQAEHHRRAFRAELCAQYDQEIILWSGGWGVQDCGFHANYDGSLQVVSGEPCSMWCTTVMQYYADCWEKCMFA"
    #word_2 = "ILIPRQQMGCFPFPWHFDFCFWSAHHSLVVPLNPQMQTVFQNRGLDRVTVKTDCHDHRWKWIYNLGLPTMTAGDWHFIKKHVVRANNPHQWFQGRLTTAWLHSTFLYKKTEYCLVRHSNCCHCDWDQIIHTCAFIAFLDLYQRHWPMCDKLYCHFHHSWFCRNQEMSMDWNQWFPWDSVPRANCLEEGALIALYAGIWANSMKRDMKTDHACTVRLIYVCELHAWLKYCYTSINMLCGNVCLRCKSWIFVKLFYMYAPVVNTIEANSPHYYKRCCILGQGICPVERKSHCEIYAKDLLSFESCCSQKQNCYTDNWGLEYRLFFQHIQMECTDPHANRGWTSCQTAKYWHFNLDDRPPKEFYMWLQATPTDLCMYQHCLMFKIVKQNFRKQHGHANPAASTSGNWDSVYTPEKMAYKDWYVSHPPVDMRRNGSKMVPVWYPPGIWHWKQSYKLTYECFFTVPGRFHVEGTFGCNRWDHQPGTRRDRQANHQFQCPYSDTMAIWEHAYTYVDQWRSIKEGQMPMSGYPNHGQWNVHDDHTNEQERSPICNQPVLAKFVRSKNVSNHEICKKSQTVFHWACEAQTNVCERMLNNQHVAVKRNVTFWWQMVPNCLWSCHNKMTWPTRPEQHRLFFVKMRLKCMHEYLDVAPSDFCRNMQAYMHSMRAILEYQADFDLKRRLRAIAPMDLCAQYDQEIILWSGGYIYDQSLQVVSCEGCSYYADCYVKCINVKEKCMFA"
    #word_1 = "PLEASANTLY"
    #word_2 = "MEANLY"
    word_1 = "GGACRNQMSEVNMWGCWWASVWVSWCEYIMPSGWRRMKDRHMWHWSVHQQSSPCAKSICFHETKNQWNQDACGPKVTQHECMRRRLVIAVKEEKSRETKMLDLRHRMSGRMNEHNVTLRKSPCVKRIMERTTYHRFMCLFEVVPAKRQAYNSCDTYTMMACVAFAFVNEADWWKCNCAFATVPYYFDDSCRMVCGARQCYRLWQWEVNTENYVSIEHAEENPFSKLKQQWCYIPMYANFAWSANHMFWAYIANELQLDWQHPNAHPIKWLQNFLMRPYHPNCGLQHKERITPLHKSFYGMFTQHHLFCKELDWRIMAHANRYYCIQHGWHTNNPMDPIDTRHCCMIQGIPKRDHHCAWSTCDVAPLQGNWMLMHHCHHWNRVESMIQNQHEVAAGIKYWRLNRNGKLPVHTADNYGVLFQRWWFLGWYNFMMWHYSLHFFAVNFYFPELNAGQMPRFQDDQNRDDVYDTCIWYFAWSNTEFMEVFGNMMMYSRPMTKMGFHGMMLPYIAINGLRSISHVNKGIGPISGENCNLSTGLHHYGQLRMVMCGYCTPYRTEVKNQREMISAVHCHQHIDWRWIWCSGHWFGSNKCDLRIEDLQNYEPAKNKSNWPYMKECRKTEPYQDNIETMFFHQHDLARDSGYIANGWHENCRQHQDFSNTFAGGHKGTPKGEHMRRSLYVWDTDCVEKCQWVPELFALCWWTPLPDGVPVMLGTYRQYMFGLVVLYWFEVKYSCHNSWDYYNFHEGTMKDSDPENWCFWGMQIIQFHDHGKPEFFQDPMKQIIKTECTAYNSFMMGHIGKTTIVYLVSYIGRLWMKSCCLTWPPYATAPIKWAEETLLDFGQGPHPKYACHFTHQNMIRLAKLPMYWLWKLMFHE"
    word_2 = "GMWGFVQVSTQSRFRHMWHWSVHQQSSECAKSICHHEWKNQWNQDACGPKVTQHECMANMPMHKCNNWFWRLVIAVKEEKVRETKMLDLIHRHWLVLNQGRMNEHNVTLRKSPCVKRIMHKWKSRTTFHRFMCLMASEVVPAKRGAQCWRQLGTYATYTVYTMMACVAFAFEYQQDNDNEADWWKCNCAFVPVYFDDSCRPVVGAFQCYRLGLPFGTGWNYAEENPFSKLKQQMHRKTMGECKNMMIWAYCANELQLPIKWGSMYHEHDFQLPPYHPNRFHKIRITILHKSFYGMFTQHHLFCKELDWRIMAWANRYYCIQHGWHTNNPDDPITRHKCMIQGGQNSRNADIRHMPVQCGNWGHAIGLEMPMPMHHCHHANRVESMIQTQHYWGPKLNRNADWWFLGWQNFEIFRMPILRWMGAYEWHYSLHFFAVNFYFPELNAGQMPRFQDDQNNNACYDVWAWSNTEFMEVNGIKKLRFGNMMMYSRPMTKMGFHGMMKSRSISHVNKGIGPISGENCSTGLHHYGQLTEVKNQREMISAVHCHQHIWCKCDLRIEPAKNKGYWPYQKEFCWRKQINSRKTEPYQVAPVINIETMFFDFWYIANGMHENCRRTGHKPNPDCVEKCQWVPELFALCWWRAMPDGVPVMLGTMFGLVVYWFEVKYSCHNSLYRRVTDYYNFHEGTMKDHEVPWNWDNEHCHDHGKAEFFFQMLKIPICDPMKAIIPSTEMVNTPWHPFSFMMGHDGKTTIVYSGSYIGRLWVPSRWKPYAPANWKMPIKWAEETLLMVPHPHFTHQQLWGTTLRLAKLPMYWLWKLMFHHLFGVK"
    D, B = wagner(word_1, word_2)
    bt = naive_backtrace(B)
     
    list1,list2 = align(word_1, word_2, bt)
    string1 = ""
    string2 = ""
    for i in range(len(list1)):
        if list1[i] != ' ':
            string1 += list1[i]
        else:
            string1 += '-'
    for i in range(len(list2)-1):
        if list2[i] != ' ':
            string2 += list2[i]
        else:
            string2 += '-'
    #print string2    
    return string1,string2


def scoringMatrix():
    lines = open('scoringMatrix.txt').read().splitlines()
    index = {letter: ind for ind, letter in enumerate(lines[0].split())}
    PAM = list(map(lambda x: list(map(int, x.split()[1:])), lines[1:]))
    #print PAM
    return PAM
 
def alphabet():
    file = open("alphabet.txt", "r")
    list1 = []
    list1 =  file.readline().strip().split(" ")
    list1 = list(filter(('').__ne__, list1))
    return list1

# def computeScore(string1, string2):
#     matrix = scoringMatrix()
#     letters = alphabet()
#     totalScore = 0
#     for i in range(0,len(string1)):
#         str1Val = string1[i]
#         str2Val = string2[i]
#         if ord(str1Val) != 45 and ord(str2Val) != 45:
#             for j in range(len(letters)):
#                 if str1Val == letters[j]:
#                     index1 = j
#                 if str2Val == letters[j]:
#                     index2 = j
#             totalScore += matrix[index1][index2]
#         else:
#             totalScore += -5
#     print totalScore
#     return totalScore


def globalAlignment():
    string1, string2 = returnTwoStrings()

    string2 += 'Y'
    print string1 + "\n"
    print string2
    score = computeScore(string1, string2)
    output = open("output.txt", "w")
    output.write(str(score))
    output.write("\n")
    output.write(string1)
    output.write("\n")
    output.write(string2)


def editDistance():
    string1, string2 = returnTwoStrings()
    string2 += 'K'
    distance = 0
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            continue
        else:
            distance += 1
    print distance
    return distance
editDistance()





#globalAlignment()



