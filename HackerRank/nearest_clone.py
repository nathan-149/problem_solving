#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#

def bfs(graph_nodes, start, adj_list, ids, val, depth):
    visited = [ False for _ in range(graph_nodes)]

    queue = [ [start, 0] ]

    while queue:
        [node, dist] = queue.pop(0)

        if(ids[node] == val and dist > 0):
            return dist

        visited[node] = True
        neighbors = adj_list[node]
        for neighbor in neighbors:
            if not visited[neighbor]:
                queue.append([neighbor, dist+1])
    return -1

def findShortest(graph_nodes, adj_list, ids, val):
    # solve here
    val_nodes = []
    for i in range(graph_nodes):
        if(ids[i] == val):
            val_nodes.append(i)

    distance = 10**6

    for node in val_nodes:
        distance = min(bfs(graph_nodes, node, adj_list, ids, val, 0), distance)
    return distance


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    adj_list = [ [] for _ in range(graph_nodes)]

    for i in range(graph_edges):
        pair = input().split()
        x = int(pair[0]) - 1
        y = int(pair[1]) - 1
        adj_list[x].append(y)
        adj_list[y].append(x)


    ids = list(map(int, input().rstrip().split()))
    ids = list(map(lambda x: x-1, ids))

    val = int(input()) - 1

    if(ids.count(val) == 0 or ids.count(val) == 1):
        ans = -1
    else:
        ans = findShortest(graph_nodes, adj_list, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
