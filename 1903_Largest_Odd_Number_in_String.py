class Solution:
    def largestOddNumber(self, nums: str) -> str:

        for i in range(len(nums)-1,-1,-1):
            if int(nums[i]) % 2 != 0:
                return nums[0:i+1]
            
        return ""