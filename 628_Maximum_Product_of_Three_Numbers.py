class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        largest = second = third = float('-inf')
        min1 = min2 = float("inf")
        for i in range(len(nums)):
            if nums[i] > largest:
                third = second
                second = largest
                largest = nums[i]
            elif nums[i] > second:
                third = second
                second = nums[i]
            elif nums[i] > third:
                third = nums[i]
            
            if nums[i] < min1:
                min2 = min1
                min1 = nums[i]
            elif nums[i] < min2:
                min2 = nums[i]
        return max(largest * second * third, largest*min1*min2)