class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(nums[0],nums[-1]):
            if i not in nums and i < nums[-1]:
                res.append(i)
        return res