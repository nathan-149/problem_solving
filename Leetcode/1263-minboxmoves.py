class Solution:

    def packString(self, box_row, box_col, player_row, player_col):
        return str(box_row) + "," + str(box_col) + "," + str(player_row) + "," + str(player_col)

    def unpackString(self, word):
        return list(map(int, word.split(",")))

    def helper(self, grid, box_row, box_col, player_row, player_col, memory, curr_steps):
        
        if(box_row < 0 or box_row >= len(grid) or box_col < 0 or box_col >= len(grid[0])):
            return 10000
        
        if(player_row < 0 or player_row >= len(grid) or player_col < 0 or player_col >= len(grid[0])):
            return 10000
        
        if(grid[box_row][box_col] == "#" or grid[player_row][player_col] == "#"):
            return 10000
        
        word = self.packString(box_row, box_col, player_row, player_col)

        if(word in memory):
            if(curr_steps < memory[word]):
                memory[word] = curr_steps
            else:
                return 10000
            
        memory[word] = curr_steps
        
        if(grid[box_row][box_col] == "T"):
            print("Hit target at: " + str(curr_steps) + " steps")
            return curr_steps
        
        val = 10000

        #Move player up
        if(player_row - 1 == box_row and player_col == box_col):
            val = min(val, self.helper(grid, box_row - 1, box_col, player_row - 1, player_col, memory, curr_steps + 1))
        else:
            val = min(val, self.helper(grid, box_row, box_col, player_row - 1, player_col, memory, curr_steps))
        
        #Move player down
        if(player_row + 1 == box_row and player_col == box_col):
            val = min(val, self.helper(grid, box_row + 1, box_col, player_row + 1, player_col, memory, curr_steps + 1))
        else:
            val = min(val, self.helper(grid, box_row, box_col, player_row + 1, player_col, memory, curr_steps))

        #Move player right
        if(player_row == box_row and player_col + 1 == box_col):
            val = min(val, self.helper(grid, box_row, box_col + 1, player_row, player_col + 1, memory, curr_steps + 1))
        else:
            val = min(val, self.helper(grid, box_row, box_col, player_row, player_col + 1, memory, curr_steps))
        
        #Move player left
        if(player_row == box_row and player_col - 1 == box_col):
            val = min(val, self.helper(grid, box_row, box_col - 1, player_row, player_col - 1, memory, curr_steps + 1))
        else:
            val = min(val, self.helper(grid, box_row, box_col, player_row, player_col - 1, memory, curr_steps))

        return val

    def minPushBox(self, grid):
        box_row = -1
        box_col = -1
        player_row = -1
        player_col = -1
        target_row = -1
        target_col = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == "B"):
                    box_row = i
                    box_col = j
                elif(grid[i][j] == "S"):
                    player_row = i
                    player_col = j
                elif(grid[i][j] == "T"):
                    target_row = i
                    target_col = j
        memory = {}
        word = self.packString(box_row, box_col, player_row, player_col)
        queue = [ [word, 0] ]
        ans = 10000

        while queue:
            [word, curr_steps] = queue.pop(0)
            
            if(word in memory and memory[word] <= curr_steps):
                print("Skip memory: " + word)
                continue
            
            memory[word] = curr_steps
            print(queue)
            print(word)

            [box_row, box_col, player_row, player_row] = self.unpackString(word)

            if(box_row < 0 or box_row >= len(grid) or box_col < 0 or box_col >= len(grid[0])):
                continue
        
            if(player_row < 0 or player_row >= len(grid) or player_col < 0 or player_col >= len(grid[0])):
                continue
            
            if(grid[box_row][box_col] == "#" or grid[player_row][player_col] == "#"):
                continue
            
            if(grid[box_row][box_col] == "T"):
                print("Hit target at: " + str(curr_steps) + " steps")
                ans = min(ans, curr_steps)
                continue
            
            

            #Move player up
            if(player_row - 1 == box_row and player_col == box_col):
                new_word = self.packString(box_row - 1, box_col, player_row - 1, player_col)
                queue.append([new_word, curr_steps + 1])
            else:
                new_word = self.packString(box_row, box_col, player_row - 1, player_col)
                queue.append([new_word, curr_steps])        
            #Move player down
            if(player_row + 1 == box_row and player_col == box_col):
                new_word = self.packString(box_row + 1, box_col, player_row + 1, player_col)
                queue.append([new_word, curr_steps + 1])  
            else:
                new_word = self.packString(box_row, box_col, player_row + 1, player_col)
                queue.append([new_word, curr_steps]) 

            #Move player right
            if(player_row == box_row and player_col + 1 == box_col):
                new_word = self.packString(box_row, box_col + 1, player_row, player_col + 1)
                queue.append([new_word, curr_steps + 1]) 
            else:
                new_word = self.packString(box_row, box_col, player_row, player_col + 1)
                queue.append([new_word, curr_steps]) 
            
            #Move player left
            if(player_row == box_row and player_col - 1 == box_col):
                new_word = self.packString(box_row, box_col - 1, player_row, player_col - 1)
                queue.append([new_word, curr_steps + 1]) 
            else:
                new_word = self.packString(box_row, box_col, player_row, player_col - 1)
                queue.append([new_word, curr_steps + 1]) 

        #print(memory)
        if(ans >= 10000):
            ans = -1
        print(ans)
        return ans
        
        
sol = Solution()
grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
sol.minPushBox(grid)

