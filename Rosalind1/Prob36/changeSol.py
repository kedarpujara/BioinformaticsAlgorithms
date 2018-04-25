def recMC(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins

#print(recMC([1,5,10,25,50],40))
#print(recMC([24,13,12,7,5,3,1],8074))

#https://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html


def coinChange(coinList,change):
	minCoins = change
	if change in coinList:
		return 1
	else:
	#coinArray = [change]
		for i in range(0,change):
			#coinArray[i] = 
			return 1



def main():
	#inputFile = open("input.txt","r")
	#change = int(inputFile.readline().strip())
	#coinList = []
	#coinList.append(inputFile.read().split(", "))
	#coinChange(coinList, change)
	coin = recMC([1,5,10,25,50],40)
	print coin

main()

