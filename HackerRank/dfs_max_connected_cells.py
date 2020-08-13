#!/bin/python3

import math
import os
import random
import re
import sys

def dfs(i, j, visited, grid):
    if(i < 0 or i >= len(grid)):
        return 0
    if(j < 0 or j >= len(grid[0])):
        return 0
    if(visited[i][j]):
        return 0
    
    visited[i][j] = True
    if(grid[i][j] == 1):
        surrounding = dfs(i+1, j, visited, grid) 
        surrounding += dfs(i-1, j, visited, grid) 
        surrounding += dfs(i, j+1, visited, grid) 
        surrounding += dfs(i, j-1, visited, grid) 
        surrounding += dfs(i+1, j+1, visited, grid) 
        surrounding += dfs(i+1, j-1, visited, grid) 
        surrounding += dfs(i-1, j+1, visited, grid) 
        surrounding += dfs(i-1, j-1, visited, grid) 
        return 1 + surrounding
    else:
        return 0

# Complete the maxRegion function below.
def maxRegion(grid):
    visited = [ [False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            result = max(dfs(i, j, visited, grid), result)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
