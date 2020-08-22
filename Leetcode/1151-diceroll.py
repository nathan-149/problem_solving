class Solution:
    def helper(self, dice_left, f, curr_sum, target, memory):
        if(dice_left < 0):
            return 0
        elif(dice_left == 0):
            if(curr_sum == target):
                return 1
            else:
                return 0
        if( (dice_left, curr_sum) in memory):
            return memory[ (dice_left, curr_sum) ]
        val = 0
        for i in range(1, f+1):
            val += self.helper(dice_left - 1, f, curr_sum + i, target, memory)
        memory[ (dice_left, curr_sum) ] = val
        return val 
            
    def numRollsToTarget(self, d, f, target):
        memory = {}
        return self.helper(d, f, 0, target, memory) % (10**9 + 7)

sol = Solution()

d = 30
f = 30
target = 500

x = sol.numRollsToTarget(d,f,target)
print(x)