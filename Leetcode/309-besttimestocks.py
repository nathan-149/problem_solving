class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if(len(prices) < 2):
        	return 0;

        #action1 means we have a stock and sell it
        #action2 means we have a stock and do nothing
        #action3 means we don't have a stock and buy a stock
        #action4 means we don't have a stock and do nothing

        
        action1 = 0;
        action2 = -prices[0];
        action3 = -prices[0];
        action4 = 0;

        for i in range(1, len(prices)):
        	l1 = action1;
        	l2 = action2;
        	l3 = action3;
        	l4 = action4;

        	#if we do action 1 on day i, then we either did action 3 or 4 on day i-1
        	#if we do action 2 on day i, then we either did action 2 or 3 on day i-1
        	#if we do action 3 on day i, then we  did action 4 on day i-1
        	#if we do action 4 on day i, then we either did action 1 or 4 on day i-1

        	action1 = max(l2, l3) + prices[i];
        	action2 = max(l2, l3);
        	action3 = l4 - prices[i];
        	action4 = max(l1, l4);

        ans = max(action1, action4);
        return ans;


sol = Solution();

print(sol.maxProfit([1,2,3,0,2]));

