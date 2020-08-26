class Solution:

    def packString(self, box_row, box_col, player_row, player_col):
        return str(box_row) + "," + str(box_col) + "," + str(player_row) + "," + str(player_col)

    def unpackString(self, state):
        return list(map(int, state.split(",")))

    def posAvailable(self, grid, row, col):
        if(row < 0 or row >= len(grid)):
            return False
        
        if(col < 0 or col >= len(grid[0])):
            return False
        
        if(grid[row][col] == "#"):
            return False
        
        return True

    def minPushBox(self, grid):
        #Setup
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
        distances = {}

        moves = [ (0,1), (0, -1), (1, 0), (-1,0) ]
        state = self.packString(box_row, box_col, player_row, player_col)
        queue = [ [state] ]

        distances[state] = 0
        
        dist = 0
        while(dist < len(queue)):
            while(queue[dist]):
                state = queue[dist].pop(0)

                if(state in memory):
                    continue
                memory[state] = 1

                [box_row, box_col, player_row, player_col] = self.unpackString(state)

                if(box_row == target_row and box_col == target_col):
                    return dist

                for move in moves:
                    new_player_row = player_row + move[0]
                    new_player_col = player_col + move[1]

                    if not self.posAvailable(grid, new_player_row, new_player_col):
                        continue

                    if(new_player_row == box_row and new_player_col == box_col):
                        L = 1
                        new_box_row = box_row + move[0]
                        new_box_col = box_col + move[1]
                    else:
                        L = 0
                        new_box_row = box_row
                        new_box_col = box_col
                    
                    if(not self.posAvailable(grid, new_box_row, new_box_col)):
                        continue

                    new_state = self.packString(new_box_row, new_box_col, new_player_row, new_player_col)

                    curr_distance = distances[state] + L
                    if(new_state not in distances or curr_distance < distances[new_state]):
                        distances[new_state] = curr_distance
                        while(len(queue) <= curr_distance):
                            queue.append([])
                        queue[curr_distance].append(new_state)
            dist += 1
        return -1
        
        
sol = Solution()
grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]

print(sol.minPushBox(grid))

