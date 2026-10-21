from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(seen,q):
            
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            while len(q)>0:
                x, y, distance = q.popleft()
                if grid[x][y] not in (0,-1):
                    grid[x][y] = min(grid[x][y], distance)
                
                for delta_x,delta_y in directions:
                    new_x = delta_x + x
                    new_y = delta_y + y
                    if new_x in range(len(grid)) and new_y in range(len(grid[0])) and (new_x, new_y) not in seen and grid[new_x][new_y] not in (-1,0):
                        q.append((new_x,new_y,distance+1))
                        seen.add((new_x,new_y))
        q = deque([])
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                   q.append((i,j,0))
        bfs(seen,q)
                    
                

