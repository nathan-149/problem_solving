class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """

        
        pack = zip(difficulty, profit);
        pack_sorted = sorted(pack);

        difficulty = [num[0] for num in pack_sorted];
        profit = [num[1] for num in pack_sorted];
        worker = sorted(worker);

        #print(difficulty);
        #print(profit);
        #print(worker);

        ans = 0;
        i = 0;
        maxProfit = 0;
        for w in worker:   
            while(i < len(difficulty) and w >= difficulty[i]):
                maxProfit = max(profit[i], maxProfit);
                i += 1;

            ans += maxProfit;
        
        return ans;


sol = Solution();


print(sol.maxProfitAssignment(
[23,30,35,35,43,46,47,81,83,98],
[8,11,11,20,33,37,60,72,87,95],
[95,46,47,97,11,35,99,56,41,92]));