class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l,r = 1,max(nums)

        while l < r:
            mid = (l + r)//2
            sums = 0
            for num in nums:
                sums += ((num + mid - 1)//mid)
            
            if sums > threshold:
                l = mid + 1
            else:
                r = mid
        return l