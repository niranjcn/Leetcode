class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            new_index = (i+k)%n
            res[new_index] = nums[i]
        nums[:] = res