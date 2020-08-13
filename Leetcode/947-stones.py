class DisjointSet:
    def __init__(self, n):
        self.parent = [ i for i in range(n) ]
        self.sizes = [1 for _ in range(n)]
        self.merged = [False for _ in range(n)]
    def find(self, stone):
        if(self.parent[stone] == stone):
            return stone
        else:
            result = self.find(self.parent[stone])
            #Path compression
            self.sizes[result] += self.sizes[stone]
            self.sizes[stone] = 0
            return result
    def union(self, x, y, stones):
        if(stones[x][0] == stones[y][0] or stones[x][1] == stones[y][1] ):
            x_parent = self.find(x)
            y_parent = self.find(y)
            if(x_parent == y_parent):
                return
            else:
                if(self.sizes[x_parent] > self.sizes[y_parent]):
                    self.parent[y_parent] = x_parent
                    self.sizes[x_parent] += self.sizes[y_parent]
                    self.sizes[y_parent] = 0
                else:
                    self.parent[x_parent] = y_parent
                    self.sizes[y_parent] += self.sizes[x_parent]
                    self.sizes[x_parent] = 0

                    
class Solution:
    def dfs(self, i, stones, rows, cols, visited):
        stone = stones[i]
        if(visited[i]):
            return 0
        visited[i] = True
        neighbors = list(set(rows[stone[0]]) | set(cols[stone[1]]))
        x = 0
        for n in neighbors:
            if not n == i and not visited[n]:
                x += 1 + self.dfs(n, stones, rows, cols, visited)
        return x

    def removeStones(self, stones):
        n = len(stones)
        visited = [ False for _ in range(n)]

        max_rows = 0
        max_cols = 0
        for stone in stones:
            max_rows = max(stone[0], max_rows)
            max_cols = max(stone[1], max_cols)

        rows = [ [] for _ in range(max_rows+1)]
        cols = [ [] for _ in range(max_cols+1)]

        for i in range(n):
            rows[stones[i][0]].append(i)
            cols[stones[i][1]].append(i)

        ans = 0
        for i in range(n):
            if not visited[i]:
                val = self.dfs(i, stones, rows, cols, visited)
                ans += max(val, 0)
        return ans
        
sol = Solution()

i =  [[0,0]]
print(sol.removeStones(i))