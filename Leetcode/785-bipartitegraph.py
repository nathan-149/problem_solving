class Solution:
    def bfs(self, graph, node):
        visited = [ False for _ in range(len(graph))]
        group = [ 0 for _ in range(len(graph))]
        # Group 0 for none
        # Group 1 for a
        # Group -1 for b

        queue = [node]
        group[node] = 1

        while queue:
            node = queue.pop(0)
            if(visited[node]):
                continue
            visited[node] = True

            for neighbor in graph[node]:
                if(group[neighbor] == 0):
                    group[neighbor] = not group[node]
                elif(group[neighbor] == group[node]):
                    return False
                queue.append(neighbor)
        return True

    def isBipartite(self, graph):
        result = False
        for i in range(len(graph)):
            if not graph[i]:
                continue
            print(str(i) + " ---- ")
            q = self.bfs(graph, i)
            print(q)
            result = result or q
        return result

sol = Solution()

x = sol.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]])

print(x)

    
            

        