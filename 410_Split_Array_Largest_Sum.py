class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(limit):
            subarray = 1
            currsum = 0

            for num in nums:
                if num + currsum > limit:
                    subarray += 1
                    currsum = num
                else:
                    currsum += num
            return subarray <= k
        
        l,r = max(nums),sum(nums)

        while l < r:
            mid = (l + r) // 2

            if canSplit(mid):
                r = mid
            else:
                l = mid + 1
        return l