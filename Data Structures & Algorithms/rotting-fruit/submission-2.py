from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque([])
        seen = set()
        max_distance = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        num_fresh_fruits = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j,0))
                if grid[i][j]==1:
                    num_fresh_fruits+=1


        while len(q)>0:
            i, j, distance = q.popleft()
            if grid[i][j] == 1:
                max_distance = max(max_distance, distance)
                num_fresh_fruits-=1
            
            for x,y in directions:
                new_x = x + i
                new_y = y + j
                if new_x in range(len(grid)) and new_y in range(len(grid[0])) and (new_x,new_y) not in seen and grid[new_x][new_y]==1:
                    q.append((new_x,new_y,distance+1))
                    seen.add((new_x,new_y))
        

        return max_distance if num_fresh_fruits==0 else -1