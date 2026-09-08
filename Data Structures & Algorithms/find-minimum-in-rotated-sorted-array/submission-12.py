class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float("inf")
        L, R = 0, len(nums)-1

        while L<=R:
            mid = (R+L) // 2
            ans = min(ans, nums[mid])
            if nums[R] < nums[mid]:
                L = mid + 1
            else:
                R = mid - 1
        return ans