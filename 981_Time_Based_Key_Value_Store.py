class TimeMap:

    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(timestamp,value)]
        else:
            self.store[key].append((timestamp,value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        arr = self.store[key]
        ans = ""
        l = 0
        r = len(arr)-1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                ans = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return ans