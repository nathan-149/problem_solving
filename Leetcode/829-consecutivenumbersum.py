import math
class Solution(object):
    def consecutiveNumbersSum(self, N):
        ans = 1
        f_N = float(N)
        k = 2.0
        while(k*(k+1)/2 <= N):
            x = (f_N - (k*(k+1)/2)) / k
            if(x%1==0):
                ans += 1
            k+=1
        return ans

sol = Solution()

print(sol.consecutiveNumbersSum(15))