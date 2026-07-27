largest = second = -1

        for i in range(len(nums)):
            if nums[i] > largest:
                second = largest
                largest = nums[i]
            elif nums[i] > second:
                second = nums[i]
        return (largest - 1)*(second - 1)