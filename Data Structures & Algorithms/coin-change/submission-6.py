class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def recurse(amount, dp_map):
            if amount==0:
                return 0
            if amount<0:
                return float("inf")
            if amount in dp_map:
                return dp_map[amount]

            ans = float("inf")
            for coin in coins:
               x = recurse(amount-coin,dp_map) + 1
               ans = min(ans,x)

            dp_map[amount] = ans
            return ans



        result = recurse(amount, {})
        return result if result!=float("inf") else -1
        