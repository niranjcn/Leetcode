class Solution:
    def longestSubarray(self, nums, k):
        prefix = {0:-1}
        res = 0
        sums = 0

        for i,num in enumerate(nums):
            sums += num
            diff = sums - k

            if diff in prefix:
                res = max(res,i - prefix[diff])
            if sums not in prefix:
                prefix[sums] = i
        return res