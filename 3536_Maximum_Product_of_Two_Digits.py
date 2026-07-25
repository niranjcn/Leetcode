class Solution:
    def maxProduct(self, n: int) -> int:
        largest = -1
        second = -1

        while n:
            digit = n % 10
            
            if digit > largest:
                second = largest
                largest = digit
            elif digit > second:
                second = digit
            
            n //= 10
        return second * largest