class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0] * (len(nums) + 1 )
        for i,num in enumerate(nums):
            prefix[i+1] = prefix[i] + num

        def mergeCount(lo,hi):
            if hi-lo <= 1:
                return 0
            mid = ( lo + hi) // 2
            count = mergeCount(lo,mid) + mergeCount(mid,hi)

            j = k = mid
            for i in range(lo,mid):
                while j < hi and prefix[j] - prefix[i] < lower: j += 1
                while k < hi and prefix[k] - prefix[i] <= upper: k += 1
                count += k - j 
            prefix[lo:hi] = sorted(prefix[lo:hi])
            return count

        return mergeCount(0,len(prefix))