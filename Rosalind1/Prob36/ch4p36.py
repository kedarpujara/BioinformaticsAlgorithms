def makeChange(money, coins):
	
	coinsDesc = sorted(coins, reverse=True)
	numCoins = 0

	for coin in coinsDesc:
		if money == 0:
			return numCoins
		if money % coin == 0:
			amount=0
			# print("money: ", money, "coin: ", coin)
			amount += money / coin
			numCoins += amount
			money -= amount * coin
		elif money % coin != 0 and money > coin: 
			# print("money: ", money, "coin: ", coin)
			amount=0
			amount += money / coin
			numCoins += amount
			money = amount % coin



	return numCoins


#rfile = open("rosalind_ba5a.txt", "r")
#money = rfile.readline().rstrip('\n')
#coins = map(int, rfile.readline().split(','))
## print("money: ", money, " coins: ", sorted(coins,reverse=True))
money = 8074
coins = [24,13,12,7,5,3,1]
print(makeChange(money, coins))
