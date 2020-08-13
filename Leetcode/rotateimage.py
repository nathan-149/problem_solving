class Solution(object):

	def rotate(self, mat):
		n = len(mat)
		print(n);
		for level in range(0, n):
			print("Level: ")
			print(level);
			for i in range(level, n-level-1):

				row = level
				col = i
				prev = mat[row][col];
				while True:
					rep = mat[col][n-row-1]
					mat[col][n-row-1] = prev;
					prev = rep;
					
					(prev_row, prev_col) = (row, col);
					row = prev_col
					col = n-prev_row-1

					if(row == level and col == i):
						break
				#mat[row][col] = prev;
		return mat

sol = Solution();

mat = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(sol.rotate90(mat));
