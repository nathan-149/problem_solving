#!/bin/python3

import math
import os
import random
import re
import sys

def find_sc_graphs(temp, v, adj_list, visited):

    visited[v] = True

    temp.append(v)

    for neighbor in adj_list[v]:
        if not visited[neighbor]:
            temp = find_sc_graphs(temp, neighbor, adj_list, visited)
    return temp

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, adj_list):
    sc_graphs = []
    visited = [ False for _ in range(n) ]
    for v in range(n):
        if not visited[v]:
            sc_graphs.append(find_sc_graphs([], v, adj_list, visited))
    
    result = 0
    for graph in sc_graphs:
        result += c_lib + c_road * (len(graph)-1)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        adj_list = [ [] for _ in range(n) ]

        for _ in range(m):
            connection = input().rstrip().split()
            x = int(connection[0])-1
            y = int(connection[1])-1
            adj_list[x].append(y)
            adj_list[y].append(x)
        
        if(c_lib <= c_road):
            result = c_lib * n
        else:
            result = roadsAndLibraries(n, c_lib, c_road, adj_list)

        fptr.write(str(result) + '\n')

    fptr.close()
