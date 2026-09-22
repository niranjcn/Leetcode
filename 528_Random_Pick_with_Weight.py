class Solution:

    def __init__(self, w: list[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        
        self.total = total

    def pickIndex(self) -> int:
        rand = random.randint(1,self.total)
        return bisect_left(self.prefix,rand)