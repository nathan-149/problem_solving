import heapq;
class Solution(object):
	def smallestRange(self, nums):
		"""
		:type nums: List[List[int]]
		:rtype:
		"""
		
		indexes = [0 for x in range(len(nums))];

		pq = [];

		minimum = 10**5;
		maximum = -10**5;

		for i,arr in enumerate(nums):
			heapq.heappush(pq, [arr[0], i]);
			maximum = max(maximum, arr[0]);
			minimum = min(minimum, arr[0]);

		ans = [minimum, maximum];

		while(pq):

			data = heapq.heappop(pq);

			if(maximum - data[0] < ans[1] - ans[0]):
				ans[1] = maximum;
				ans[0] = data[0];

			arr = data[1];
			indexes[arr] += 1;

			if(indexes[arr] == len(nums[arr])):
				return ans;
			new = nums[arr][indexes[arr]];
			maximum = max(maximum, new);
			heapq.heappush(pq, [new, arr]);

		return ans;

sol = Solution();

x = sol.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]);

print(x);