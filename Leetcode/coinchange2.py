class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp = [amount+1] * (amount+1);
        dp[0] = 0;
        coins.sort(reverse = True);
        for c in coins:
            for i in range(c, amount+1):
                dp[i] = min(dp[i-c]+1, dp[i]);
            #print(dp);
        return (dp[amount] if dp[amount] != amount + 1 else -1);

sol = Solution();

print(sol.coinChange([1,3, 5], 8));