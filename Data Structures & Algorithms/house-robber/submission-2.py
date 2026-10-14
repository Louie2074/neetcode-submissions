class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_map = {}
        x = self.dp(0, 0, nums, dp_map)
        return x


    def dp(self,index, sum,nums, dp_map):
        if not index in range(len(nums)):
            return sum
        if (index,sum) in dp_map:
            return dp_map[(index,sum)]

        one = self.dp(index+1,sum,nums,dp_map)
        two = self.dp(index+2, sum+nums[index],nums,dp_map)

        ans = max(one,two)
        dp_map[(index,sum)] = ans

        return ans
