class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        l = 0
        for r in range(1,len(nums)):
            if nums[r] - nums[l] > k:
                res += 1
                l = r
        return res + 1