class Solution(object):

	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		#coins.sort();

		if amount == 0:
			return 0;

		arr = [-1 for x in range(amount + 1)];
		arr[0] = 0;

		for c in range(len(coins)):
			for a in range(amount + 1):
				if a-coins[c] >= 0 and arr[a-coins[c]] >= 0:
					if arr[a] >= 0:
						arr[a] = min(arr[a], arr[a-coins[c]] + 1);
					else:
						arr[a] = arr[a-coins[c]] + 1;

		#print(arr);
		
		return arr[amount];



sol = Solution();

print(sol.coinChange([186,419,83,408], 6249));
