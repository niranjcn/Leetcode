class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candie = max(candies)
        res = []
        for candy in candies:
            if candy + extraCandies >= max_candie:
                res.append(True)
            else:
                res.append(False)
        return res