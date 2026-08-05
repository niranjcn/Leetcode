class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_II(nums):
            
            dp = [0] * (len(nums)+2)

            for i in range(len(nums)-1,-1,-1):
                dp[i] = max((nums[i] + dp[i+2]),dp[i+1])
        
            return dp[0]
        
        return max(rob_II(nums[:-1]),rob_II(nums[1:]))