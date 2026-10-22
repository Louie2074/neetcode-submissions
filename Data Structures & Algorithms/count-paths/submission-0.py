class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(x,y,memo):
            if x >= m or y >= n:
                return 0
            if x == m-1 and y == n-1:
                return 1
            if memo[x][y] != -1:
                return memo[x][y]
            # if its 1xn then 1

            memo[x][y] = dfs(x, y+1, memo) + dfs(x+1, y, memo)
            return memo[x][y]
            
        memo = [[-1] * n for _ in range(m)]
        return dfs(0,0,memo)
       