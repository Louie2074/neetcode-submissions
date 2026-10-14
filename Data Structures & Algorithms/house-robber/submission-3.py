class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_map = {}
        x = self.dp(0, nums, dp_map)
        return x


    def dp(self,index,nums, dp_map):
        if not index in range(len(nums)):
            return 0
        if index in dp_map:
            return dp_map[index]

        one = self.dp(index+1,nums,dp_map)
        two = nums[index] + self.dp(index+2,nums,dp_map)

        ans = max(one,two)
        dp_map[index] = ans
        return ans
