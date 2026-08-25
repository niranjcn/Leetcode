class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        distance = 0

        for point in points:
            distance = sqrt(((0 - point[0])**2) + ((0 - point[1])**2))

            heapq.heappush(heap,(-distance,point))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [point for distance, point in heap]