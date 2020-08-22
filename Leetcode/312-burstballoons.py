class Solution:
    
    def maxCoins(self, nums):
        if(len(nums) == 0):
            return 0
        dp = [ [ 0 for _ in range(len(nums)) ] for _ in range(len(nums)) ]

        for length in range(len(nums)):
            #print(dp)
            for start in range(len(nums)):
                end = start + length
                if(end >= len(nums)):
                    continue
                
                max_val = 0
                for i in range(start, end+1):
                    # Calculate left, right, mid
                    if(i - 1 < 0):
                        left = 0
                    else:
                        left = dp[start][i-1] 

                    if(i + 1 >= len(nums)):
                        right = 0
                    else:
                        right = dp[i+1][end]

                    if(start - 1 < 0): 
                        x = 1
                    else: 
                        x = nums[start - 1]

                    if(end + 1 >= len(nums)):
                        y = 1
                    else:
                        y = nums[end+1]

                    mid = x * nums[i] * y

                    val = left + mid + right
                    if(val >= max_val):
                        max_val = val
    
                dp[start][end] = max_val

        return dp[0][len(nums) - 1]

sol = Solution()

x = [3,1,5,8]
ans = sol.maxCoins(x)
print(ans)

