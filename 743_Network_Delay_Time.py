class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))
        
        minHeap = [(0,k)]
        t = 0
        visited = set()

        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            
            visited.add(n1)
            t = max(t,w1)

            for n2,w2 in edges[n1]:
                if n2 in visited:
                    continue
                heapq.heappush(minHeap,(w1+w2,n2))
        
        return t if len(visited) == n else -1