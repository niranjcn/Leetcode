class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        graph = defaultdict(list)
        inDegree = [0] * numCourses

        for course, pre in prereq:
            graph[pre].append(course)
            inDegree[course] += 1
        
        q = deque()
        for course in range(numCourses):
            if inDegree[course] == 0:
                q.append(course)

        finished = 0

        while q:
            course = q.popleft()
            finished += 1

            for nei in graph[course]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)
        return finished == numCourses