class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            rob = nums[i] + dfs(i+2)
            skip = dfs(i+1)

            memo[i] = max(rob,skip)

            return memo[i]
        return dfs(0)