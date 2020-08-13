class Solution(object):

    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """

        store = [[[0 for x in range(0, N)] for y in range(0, N)] for z in range(0, K+1)];

        store[0][r][c] = 1;

        for k in range(1, K+1):
            for r in range(0, N):
                for c in range(0, N):
                    if(r - 2 >= 0 and c + 1 < N):
                        r2 = r - 2;
                        c2 = c + 1;
                        store[k][r][c] += store[k-1][r2][c2];
                    if(r - 2 >= 0 and c - 1 >= 0):
                        r2 = r - 2;
                        c2 = c - 1;
                        store[k][r][c] += store[k-1][r2][c2];
                    if(r + 2 < N and c + 1 < N):
                        r2 = r + 2;
                        c2 = c + 1;
                        store[k][r][c] += store[k-1][r2][c2];
                    if(r + 2 < N and c - 1 >= 0):
                        r2 = r + 2;
                        c2 = c - 1;
                        store[k][r][c] += store[k-1][r2][c2];
                    if(c - 2 >= 0 and r - 1 >= 0):
                        r2 = r - 1;
                        c2 = c - 2;
                        store[k][r][c] += store[k-1][r2][c2];
                    if(c - 2 >= 0 and r + 1 < N):
                        r2 = r + 1;
                        c2 = c - 2;
                        store[k][r][c] += store[k-1][r2][c2];
                    if(c + 2 < N and r - 1 >= 0):
                        r2 = r - 1;
                        c2 = c + 2;
                        store[k][r][c] += store[k-1][r2][c2];
                    if(c + 2 < N and r + 1 < N):
                        r2 = r + 1;
                        c2 = c + 2;
                        store[k][r][c] += store[k-1][r2][c2];
        ans = 0.0;
        for i in range(0, N):
            for j in range(0, N):
                ans += store[K][i][j];
                
        return ans / (8.0**K);



sol = Solution();

print(sol.knightProbability(3, 2, 0, 0));

