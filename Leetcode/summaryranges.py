class Solution(object):


    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        #edge case: empty list
        if(len(nums) == 0):
        	return [];

        #edge case: one element
        if(len(nums) == 1):
        	return [str(nums[0])];

        start = nums[0];
        ans = [];

        for i in range(1, len(nums)):

        	
        	x = nums[i-1];
        	y = nums[i];

        	#not consecutive
        	if(x+1 != y):
        		if start == x:
        			ans.append(str(x));
        		else:
        			ans.append(str(start) + "->" + str(x));

        		start = y;

        	#consecutive, do nothing

        	#reached the end of nums
        	if(i == len(nums) - 1):
        		if start == y:
        			ans.append(str(y));
        		else:
        			ans.append(str(start) + "->" + str(y));

        return ans;
        	
        
sol = Solution();

nums = [0,1,2,4,5,7];

a = sol.summaryRanges(nums);

for b in a:
	print(b);