class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights),sum(weights)
        while l < r:
            mid = (l+r)//2
            capacity = 0
            days_used = 1

            for wei in weights:
                capacity += wei
                if capacity > mid:
                    days_used += 1
                    capacity = wei
            
            if days_used > days:
                l = mid + 1
            else:
                r = mid
        return l