class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(x,y,seen,sub_word):
            directions = [(0,1),(1,0), (-1,0), (0,-1)]

            if len(sub_word) == 0:
                return True


            for delta_x, delta_y in directions:
                new_x = delta_x + x
                new_y = delta_y + y
                if new_x in range(len(board)) and new_y in range(len(board[0])) and board[new_x][new_y] == sub_word[0] and (new_x,new_y) not in seen:  
                    seen.add((x,y))          
                    ans = backtrack(new_x,new_y, seen, sub_word[1:])
                    if ans:
                        return True
                    seen.remove((x,y))

        
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    seen = set()
                    found = backtrack(i,j,seen,word[1:])
                    if found:
                        return True
        return False

        