'''
BytelandianGoldCoins ID346
In Byteland they have a very strange monetary system.

Each Bytelandian gold coin has an integer number written on it. A coin n can be exchanged in a bank into three coins: n/2, n/3 and n/4. 
But these numbers are all rounded down (the banks have to make a profit).

You can also sell Bytelandian coins for American dollars. The exchange rate is 1:1. But you can not buy Bytelandian coins.

You have one gold coin. What is the maximum amount of American dollars you can get for it?

Input
The input will contain several test cases (not more than 10). Each testcase is a single line with a number n, 0 <= n <= 1 000 000 000. It is the number written on your coin.

Output
For each test case output a single line, containing the maximum amount of American dollars you can make.

Input:
12
2

Output:
13
2

'''

#better to use a global dictionary, stores values from one test case to another
max_exchange_dict = dict()

#exchange coins for profit
def exchange_coins(coin_val):
	if coin_val <=4:
		return coin_val

	if coin_val in max_exchange_dict.keys():
		return max_exchange_dict[coin_val]

	max_val_after_exhange = max(coin_val, exchange_coins(coin_val//2) + exchange_coins(coin_val//3) + exchange_coins(coin_val//4))
	max_exchange_dict[coin_val] = max_val_after_exhange
	return max_exchange_dict[coin_val]


try:
	while True:
		coin_val = int(input())
		max_possible_exchange = exchange_coins(coin_val)
		print(max_possible_exchange)
except:
	pass