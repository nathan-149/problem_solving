class Graph:
    def __init__(self, n, m, adj_list):
        self.n = n
        self.m = m
        self.adj_list = adj_list

    def find_all_distances(self, start):
        #bfs
        result = [-1 for _ in range(n)]
        visited = [False for _ in range(n)]

        queue = [ [start, 0] ]

        while queue:
            [node, dist] = queue.pop(0)
            if not visited[node]:
                visited[node] = True
                result[node] = dist
            else:
                continue
            
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    queue.append([neighbor, dist+6])

        result.pop(start)
        return result

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,m = [int(value) for value in input().split()]
        adj_list = [ [] for _ in range(n)]
        for i in range(m):
            x,y = [int(x) for x in input().split()]
            x = x-1
            y = y-1
            adj_list[x].append(y)
            adj_list[y].append(x)
        graph = Graph(n, m, adj_list)    
        s = int(input())
        result = graph.find_all_distances(s-1)
        for node in result:
            print(str(node) + ' ', end="")
        print("")
