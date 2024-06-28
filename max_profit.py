import numpy as np
from tqdm import tqdm
import random

def labeling(f):
	def wrapper(*args):
		buy,sell,prof = f(*args)
		# print(prices)
		print(f" buy time: {buy}")
		print(f"sell time: {sell}")
		print(f"   profit: {prof}")
	return wrapper

@labeling
def max_profit(prices):
	best_buy_time = 0
	best_sell_time = 0
	best_profit = 0
	can_buy_time = 0 
	can_sell_time = 0

	for i in tqdm(range(len(prices[1:]))):
		i+=1
		today_price = prices[i]
		
		if today_price > prices[can_sell_time]:	
			can_sell_time = i
		if today_price < prices[can_buy_time]:
			can_buy_time = i
			can_sell_time = i
	
		can_profit = prices[can_sell_time] - prices[can_buy_time]
		unrealized_prof = prices[can_sell_time] - prices[best_buy_time]

		if can_profit > best_profit:
			best_profit = can_profit
			best_buy_time = can_buy_time
			best_sell_time = can_sell_time
		
		if unrealized_prof > best_profit:
			best_sell_time = can_sell_time
		
	return best_buy_time, best_sell_time, best_profit

@labeling
def new_max_profit(prices):
	profit = 0
	buy_time = 0
	sell_time = 0

	pot_buy_time  = 0
	for i, price in enumerate(tqdm(prices)):
		if price < prices[pot_buy_time]:
			pot_buy_time = i

		if profit < price - prices[pot_buy_time]:
			profit = price - prices[pot_buy_time]
			buy_time = pot_buy_time
			sell_time = i

	return buy_time, sell_time, profit

if __name__ == "__main__":
	cases = [
		# np.arange(10),
		# np.arange(10)[::-1],
		# [10,11, 1,9,8,8,8,8],
		# [10,15,1,4,4,4,4],
		# [10,1,4,3,7,6,8],
		np.random.randint(0,100,size=1000)
	]
	# prices = np.arange(10)[::-1]
	# prices = [10,11, 1,9,8,8,8,8]
	# prices = [10,15,1,4,4,4,4]
	# prices = [10,1,4,3,7,6,8]
	for prices in cases:
		new_max_profit(prices)




