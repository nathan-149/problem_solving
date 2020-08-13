class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        out = [1] * len(nums);

        total = 1;
        for i in range(len(nums)-1, -1, -1):
            out[i] = total;
            total *= nums[i];
        #print(nums);
        #print(out);


        left = 1;
        for i in range(1, len(nums)):
            left *= nums[i-1];
            total = out[i] * left;
            #print("left",left);
            #print("out",out[i]);
            out[i] = total;

        return out;
    
sol = Solution();

arr = [1,2,3];

print(sol.productExceptSelf(arr));

