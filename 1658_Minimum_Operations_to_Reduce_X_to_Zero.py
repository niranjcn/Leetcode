class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        window_sum = 0
        res = -1
        l = 0

        if target < 0:
            return -1
        
        if target == 0:
            return len(nums)

        for r in range(len(nums)):
            window_sum += nums[r]
            while window_sum > target:
                window_sum -= nums[l]
                l += 1
            if window_sum == target:
                res = max(res,(r-l+1))

        return len(nums)-res if res != -1 else -1