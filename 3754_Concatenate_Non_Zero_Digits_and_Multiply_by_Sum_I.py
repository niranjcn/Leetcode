class Solution:
    def sumAndMultiply(self, nums: int) -> int:
        n,sums = 0,0
        i = 0
        while nums > 0:
            digit = nums % 10
            if digit != 0:
                n += digit * (10 ** i)
                i += 1
                sums += digit
            nums = nums//10
        return n * sums