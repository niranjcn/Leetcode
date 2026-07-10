class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0,len(nums)-1
        res = [0] * len(nums)
        i = len(nums)-1
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                res[i] = nums[r]*nums[r]
                r -= 1
            else:
                res[i] = nums[l]*nums[l]
                l += 1
            i -= 1
                
        return res