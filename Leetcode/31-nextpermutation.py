class Solution:
    def nextPermutation(self, nums):
        x = -1
        min_val = 10**6
        min_index = -1
        for i in range(0, len(nums)-1):
            if nums[i] < nums[i+1]:
                x = i

        if x == -1:
            nums.reverse()
            return

        for i in range(x+1, len(nums)):
            # If we found permutation change opportunity
                if(nums[i] <= min_val and nums[i] > nums[x]):
                    min_val = nums[i]
                    min_index = i
        
        temp = nums[x]
        nums[x] = nums[min_index]
        nums[min_index] = temp
        
        first = nums[0:x+1]
        second = nums[x+1:]
        second.reverse()
        result = first + second

        for i in range(x+1, len(nums)):
            upper = len(nums) - 1 - (i - (x+1))
            if(i > upper):
                break
            temp = nums[i]
            nums[i] = nums[upper]
            nums[upper] = temp
