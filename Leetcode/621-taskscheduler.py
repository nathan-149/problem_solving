from heapq import *

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dictionary = {};
        p_queue = [];
        count = 0;

        for elem in tasks:
        	if(elem in dictionary):
        		dictionary[elem] -= 1;
        	else:
        		dictionary[elem] = -1;

        for elem in dictionary:
        	heappush(p_queue, dictionary[elem]);

        
        while p_queue:
        	temp = [];
        	for i in range(0, n + 1):
        		if not p_queue:
        			break;
        		temp.append(heappop(p_queue));

        	for elem in temp:
        		if(elem + 1 < 0):
        			heappush(p_queue, (elem + 1));

        	if not p_queue:
        		count += len(temp);
        	else:
        		count += n+1;

       	return count;

sol = Solution();

tasks = ["A","A","A","B","B","B"];
n = 2;
print(sol.leastInterval(tasks, n));

