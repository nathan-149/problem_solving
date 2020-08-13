class Solution(object):

	
	def BFS(self, vertex, visited, graph):
		queue = [[vertex]];
		visited[vertex] = True;
		depth = 0;

		while len(queue) > 0:
			
			path = queue.pop(0);

			curr = path[-1];

			visited[curr] = True;
			#print("path:", path);		

			for neighbor in graph[curr]:
				if not visited[neighbor]:
					newPath = list(path);
					newPath.append(neighbor)
					queue.append(newPath);	
					#print("added:", newPath);	
						

		return path;


	def findMinHeightTrees(self, n, edges):
		"""
		:type n: int
		:type edges: List[List[int]]
		:rtype: List[int]
		"""
		graph = [];
		for i in range(0, n):
			graph.append([]);
		leaves = [];

		for edge in edges:
			first = edge[0];
			second = edge[1];
			graph[first].append(second);
			graph[second].append(first);

		visited = [False] * n;
		path1 = self.BFS(0, visited, graph);
		v1 = path1[-1];
		

		visited = [False] * n;
		traversal = self.BFS(v1, visited, graph);
		length = len(traversal);

		ans = [];
		ans.append(traversal[length // 2]);
		if(length % 2 == 0):
			ans.append(traversal[(length // 2) - 1]);

		print(ans);
		return ans;


sol = Solution();
n = 6; 
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]];

sol.findMinHeightTrees(n, edges);













