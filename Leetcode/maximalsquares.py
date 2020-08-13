class Solution(object):


    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        ans = 0;
        inc = True;

        while len(matrix) > 0 and len(matrix[0]) > 0 and inc == True:
            inc = False;
            for i in range(0, len(matrix)):
                for j in range(0, len(matrix[0])):
                    #edge case for just a single one
                    if ans == 0 and matrix[i][j] == '1':
                        ans = 1;

                    #make smaller squares
                    if i + 1 < len(matrix) and j + 1 < len(matrix[0]):
                        if matrix[i][j] == '1' and matrix[i][j+1] == '1' and matrix[i+1][j] == '1' and matrix[i+1][j+1] == '1':
                            if not inc:
                                ans += 1;
                            inc = True;
                            matrix[i][j] = '1';
                        else:
                            matrix[i][j] = '0';

            matrix = [matrix[x][0:len(matrix[0]) - 1] for x in range(0, len(matrix) - 1)];
            print(matrix)

        return ans*ans;
      

sol = Solution();

matrix = [ [0,0,1,0,0], 
           [1,0,1,1,1],
           [1,1,1,1,1],
           [1,0,1,1,0] ];

matrix =[["1","1","1","1"],
         ["1","1","1","1"],
         ["1","1","1","1"]]

print(sol.maximalSquare(matrix));


