class Solution:
    def openLock(self, deadends, target):
        length = 0
        queue = [["0000", 0]]
        de_dict = {}
        for de in deadends:
            de_dict[de] = 1
        
        visited = {  }

        while(queue):
            [curr, dist] = queue.pop(0)
            if(curr in visited):
                continue
            visited[curr] = 1
            if(curr in de_dict):
                continue

            if(curr == target):
                return dist
            
            for i in range(len(curr)):
                c = int(curr[i])
                if(c == 0):
                    up = 1
                    down = 9
                elif(c == 9):
                    up = 0
                    down = 8
                else:
                    up = c+1
                    down = c-1

                if(i == len(curr) - 1):
                    new_up = curr[0:i] + str(up)
                    new_down = curr[0:i] + str(down)
                else:
                    new_up = curr[0:i] + str(up) + curr[(i+1):]
                    new_down = curr[0:i] + str(down) + curr[(i+1):]
                queue.append([new_up, dist+1])
                queue.append([new_down, dist+1])
        return -1

sol = Solution()

deadends = deadends = ["8888"]
target = "0009"

x =sol.openLock(deadends,target)
print(x)
