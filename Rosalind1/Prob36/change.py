def change(money, coins):

	minNimCoins = [0] * money
	
	for m in range(1,money):
		minNimCoins[m] = 9999999999999999
		for i in range(1,len(coins)):
			if m >= coins[i-1]:
				if (minNimCoins[m-coins[i-1]] + 1) < minNimCoins[m]:
					minNimCoins[m] = minNimCoins[m-coins[i-1]] +1
					#print minNimCoins[m]
	return minNimCoins[money-1]


money = 40
coins = [1,5,10,20,25,50]
coins2 = [24,13,12,7,5,3,1]
numRet = change(money, coins)
#print numRet



def change2(money, coins):
	coinList = sorted(coins, reverse=True)
	minCoins = 0
	for coin in coinList:
		if money == 0:
			return minCoins
		if money % coin == 0:
			moneyLeft = 0
			moneyLeft += money/coin
			minCoins += moneyLeft
			money -= moneyLeft*coin
		elif money % coin != 0 and money > coin:
			moneyLeft = 0
			moneyLeft += money/coin
			minCoins += moneyLeft
			money = moneyLeft%coin
	return minCoins


money = 17031
coins = [1,3,5]

print(change2(money, coins))
