class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        def to_seconds(time):
            splitTime = time.split(":")
            hrs = int(splitTime[0])
            mins = int(splitTime[1])
            sec = int(splitTime[2])
            return hrs * 3600 + mins* 60 + sec
        return (to_seconds(endTime) - to_seconds(startTime))