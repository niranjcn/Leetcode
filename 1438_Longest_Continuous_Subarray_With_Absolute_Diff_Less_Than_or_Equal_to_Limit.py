class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        l = 0
        maxq = deque()
        minq = deque()
        
        for r in range(len(nums)):
            while maxq and  nums[r] > nums[maxq[-1]]:
                maxq.pop()
            maxq.append(r)
            while minq and  nums[r] < nums[minq[-1]]:
                minq.pop()
            minq.append(r)
            while nums[maxq[0]] - nums[minq[0]] > limit:
                if maxq[0] == l:
                    maxq.popleft()
                if minq[0] == l:
                    minq.popleft()
                l += 1
            res = max(res,r-l+1)
                
        return res