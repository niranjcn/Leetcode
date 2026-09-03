class Solution:
    def check(self, nums: List[int]) -> bool:
        point = 0
        if nums[0] < nums[-1]:
            point += 1
        
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                point += 1
        return True if point < 2 else False