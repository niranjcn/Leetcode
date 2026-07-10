class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res,cursum = 0,0
        prefix = {0 : 1}

        for num in nums:
            cursum += num
            diff = cursum - k

            res += prefix.get(diff,0)
            prefix[cursum] = 1 + prefix.get(cursum,0)
        return res