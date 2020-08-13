import heapq 

class Solution(object):

    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        data = [];
        ans = [];

        heap = [];
        heapq.heapify(heap); 
        
        #parse input
        for b in buildings:
            start = [b[0], b[2]];
            end = [b[1], -b[2]];
            data.append(start);
            data.append(end);

        data = sorted(data);

        #print(data);

        i = 0;
        maximum = 0;
        heapq.heappush(heap, 0);
        while(i < len(data)): 
            change = False;

            #do while loop for same indexes
            while(True):
                
                x = data[i][0];
                height = data[i][1];
                #print("curr", x);
                #print("Heap", heap);

                #case for start
                if(height > 0): 
                    heapq.heappush(heap, -height);
                    if(height > maximum):
                        
                        change = True;
                        maximum = height;

                #case for end
                else:

                    #REMOVING SLOW ASF
                    j = heap.index(height);
                    heap.pop(j);
                    heapq.heapify(heap);

                    if(abs(height) == maximum):
                        
                        change = True;
                        maximum = -heap[0];
                i += 1;
                if(i >= len(data) or data[i-1][0] != data[i][0]):
                    break;
            
            #add it to the answer
            if change:
                if(len(ans) == 0):
                    ans.append([x, maximum]);
                elif(ans[-1][1] != maximum):
                    ans.append([x, maximum]);

        return ans;


sol = Solution();

print(sol.getSkyline([ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]))