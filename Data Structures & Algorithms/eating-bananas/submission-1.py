class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = float("inf")
        L, R = 1, max(piles)+1
        while L<=R:
            mid = (R+L)//2
            is_valid = self.total_time(mid, piles,h)
            if not is_valid:
                L = mid+1
            else:
                ans = min(ans, mid)
                R = mid -1
        return ans
        
    def total_time(self, divisor, piles,h):
        total_time = 0
        for pile in piles:
            total_time += math.ceil(pile / divisor)
        return total_time <= h