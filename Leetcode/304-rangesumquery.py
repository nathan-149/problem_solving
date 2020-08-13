class NumMatrix(object):

    matrix = [];
    
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        

# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]];
obj = NumMatrix(matrix)
#param_1 = obj.sumArr(0,0, 0, 4, 0);
param_1 = obj.sumRegion(2,1,4,3)
print(param_1);