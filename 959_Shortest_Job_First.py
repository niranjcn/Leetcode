class Solution:
    def solve(self, bt):
        bt.sort()

        total_wait = 0
        current_wait = 0

        for i in range(len(bt)):
            total_wait += current_wait
            current_wait += bt[i]
            
        return total_wait // len(bt)