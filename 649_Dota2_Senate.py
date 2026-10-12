class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        rad = deque()
        dire = deque()

        for i,ch in enumerate(senate):
            if ch == "R":
                rad.append(i)
            else:
                dire.append(i)
        
        while rad and dire:
            r = rad.popleft()
            d = dire.popleft()

            if r < d:
                rad.append(r + len(senate))
            else:
                dire.append(d + len(senate))
        return "Radiant" if rad else "Dire"