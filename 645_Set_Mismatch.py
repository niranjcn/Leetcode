class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        i,j = 0,0
        for num in nums:
            if num in seen:
                i = num
            seen.add(num)
        for x in range(1,len(nums)+1):
            if x not in seen:
                j = x
        return [i,j]