class Solution(object):
	#POP OUT AT DA PARTY, IM WIT DA GANG

	def profitableSchemes(self, G, P, group, profit):
		"""
		:type G: int
		:type P: int
		:type group: List[int]
		:type profit: List[int]
		:rtype: int
		"""	
		
		memory = [[0 for x in range (0, G + 1)] for y in range (0, P + 1)];

		memory[0][G] = 1;
		
		for crime in range(0, len(group)):
			g = group[crime];
			p = profit[crime];

			for i in range(P, -1, -1):
				for j in range(0, G+1):
					if(j - g >= 0):
						memory[min(i+p, P)][j-g] += memory[i][j];
		ans = 0;

		for j in range(0, G+1):
			ans += memory[P][j];
		return ans %;



sol = Solution();
#G = 5, P = 3, group = [2,2], profit = [2,3]
#G = 10, P = 5, group = [2,3,5], profit = [6,7,8]
#print(sol.profitableSchemes(5, 3, [2,2], [2,3]));
#print(sol.profitableSchemes(10, 5, [2,3,5], [6,7,8]));
#print(sol.profitableSchemes(1, 1, [1], [1]));


p = [2,5,36,2,5,5,14,1,12,1,14,15,1,1,27,13,6,59,6,1,7,1,2,7,6,1,6,1,3,1,2,11,3,39,21,20,1,27,26,22,11,17,3,2,4,5,6,18,4,14,1,1,1,3,12,9,7,3,16,5,1,19,4,8,6,3,2,7,3,5,12,6,15,2,11,12,12,21,5,1,13,2,29,38,10,17,1,14,1,62,7,1,14,6,4,16,6,4,32,48]

g = [21,4,9,12,5,8,8,5,14,18,43,24,3,0,20,9,0,24,4,0,0,7,3,13,6,5,19,6,3,14,9,5,5,6,4,7,20,2,13,0,1,19,4,0,11,9,6,15,15,7,1,25,17,4,4,3,43,46,82,15,12,4,1,8,24,3,15,3,6,3,0,8,10,8,10,1,21,13,10,28,11,27,17,1,13,10,11,4,36,26,4,2,2,2,10,0,11,5,22,6]
print(sol.profitableSchemes(100, 100, p, g));