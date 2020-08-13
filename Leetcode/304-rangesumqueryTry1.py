class NumMatrix(object):

    stMatrix = [];
    matrix = [];
    
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix;
        self.stMatrix = [];
        for i in range(len(matrix)):
            st = [0 for x in range(len(matrix[i]) * 2 + 1)];
            self.constructST(matrix[i], 0, len(matrix[i]) - 1, st, 0);
            self.stMatrix.append(st);

    def constructST(self, arr, start, end, st, curr):

        if(start == end):
            st[curr] = arr[start];
            return arr[start];

        mid = (start + end) // 2;

        st[curr] = self.constructST(arr, start, mid, st, curr * 2 + 1) + \
                   self.constructST(arr, mid+1, end, st, curr * 2 + 2);
        return st[curr];

    def sumArr(self, st, qstart, qend, start, end, curr):
        #case 1: complete overlap return node
        if(qstart <= start and qend >= end):

            return st[curr];

        #case 2: no overlap return 0
        if(qstart > end or qend < start):
            return 0;

        #case 3: partial overlap return sum of left and right
        if(qstart >= start and qstart <= end or qend >= start and qend <= end):
            mid = (start + end) // 2;
            return self.sumArr(st, qstart,qend, start, mid, curr*2+1) + self.sumArr(st, qstart,qend, mid+1, end, curr*2+2);

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans = 0;

        #print(len(self.stMatrix));

        #for i in range(len(self.stMatrix)):
        #    print(self.stMatrix[i]);

        if not self.matrix:
            return 0;

        for r in range(row1, row2+1):
            ans += self.sumArr(self.stMatrix[r], col1, col2, 0, len(self.matrix[r]) - 1, 0);
        return ans;

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