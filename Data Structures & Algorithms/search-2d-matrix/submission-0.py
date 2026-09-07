class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L , R = 0, len(matrix)-1
        while L <= R:
            mid = L + (R-L) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                L2 , R2 = 0, len(matrix[mid])-1
                while L2 <= R2:
                    mid2 = L2 + (R2-L2) // 2
                    if matrix[mid][mid2]==target:
                        return True
                    elif matrix[mid][mid2] > target:
                        R2 = mid2 -1
                    else:
                        L2 = mid2 + 1    
                return False
            elif matrix[mid][0] > target:
                R = mid -1
            else:
                L = mid + 1
        return False
