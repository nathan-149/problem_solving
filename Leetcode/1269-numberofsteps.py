class Solution:
    def numWays(self, steps, arrLen):

        #Optimize with max_index
        max_index = min(steps+1,arrLen)
        dp = [ [ 0 for _ in range(max_index)] for _ in range(steps) ]
        dp[0][0] = 1
        dp[0][1] = 1
        for i in range(1, steps):
            for j in range(max_index):
                # 3 cases: stay, right, left
                dp[i][j] = dp[i-1][j]
                if(j-1 >= 0):
                    dp[i][j] += dp[i-1][j-1]
                if(j+1 < max_index):
                    dp[i][j] += dp[i-1][j+1]
        #print(dp)
        return dp[steps-1][0] % (10**9 + 7)

sol = Solution()
x = 5
arrLen = 5
ans = sol.numWays(x, arrLen)
print(ans)


        