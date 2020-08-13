#!/bin/python3

import math
import os
import random
import re
import sys

class DisjointSet:
    def __init__(self, size):
        self.parent = [ i for i in range(size) ]
        
    def find(self, node):
        if(self.parent[node] == node):
            return node
        else:
            result = self.find(self.parent[node])
            #Path compression
            self.parent[node] = result
            return result

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if(x == y):
            return
        self.parent[x] = y

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machines = []

    for _ in range(k):
        machines_item = int(input())
        machines.append(machines_item)

    sorted_roads = sorted(roads, key=lambda x: x[2], reverse=True)

    cities_set = DisjointSet(n)

    result = 0

    m = [ False for _ in range(n)]
    for index in machines:
        m[index] = True
    
    for [x,y,cost] in sorted_roads:
        x = cities_set.find(x)
        y = cities_set.find(y)
        if(m[x] and m[y]):
            result += cost
        else:
            cities_set.union(x, y)
            m[x] = m[x] or m[y]
            m[y] = m[x] or m[y]
        
    fptr.write(str(result) + '\n')

    fptr.close()
