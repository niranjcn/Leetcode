class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l,r = min(bloomDay),max(bloomDay)

        if len(bloomDay) < m * k:
            return -1

        while l < r:
            mid = (l+r)//2

            flower = 0
            bouquet = 0

            for day in bloomDay:
                if day <= mid:
                    flower += 1
                    if flower == k:
                        bouquet += 1
                        flower = 0
                else:
                    flower = 0
                
            if bouquet >= m:
                r = mid
            else:
                l = mid + 1
        return l