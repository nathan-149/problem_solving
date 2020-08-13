class Solution(object):
	def mincostTickets(self, days, costs):
		"""
		:type days: List[int]
		:type costs: List[int]
		:rtype: int
		"""

		arr = [0 for x in range(366)];
		travelDay = [False for x in range(365+1)];

		for d in days:
			travelDay[d] = True;

		for i in range(1, 366):
			if(travelDay[i]):

				x = arr[i - 1] + costs[0];

				if(i >= 7):
					x = min(x, arr[i - 7] + costs[1]);
				else:
					x = min(x, costs[1]);

				if(i >= 30):
					x = min(x, arr[i - 30] + costs[2]);
				else:
					x = min(x, costs[2]);
				arr[i] = x;
			else:
				arr[i] = arr[i-1];

		ans = arr[365];
		#print(arr);
		return ans;

sol = Solution();

print(sol.mincostTickets([1,4,6,7,8,20],[2,7,15]));
