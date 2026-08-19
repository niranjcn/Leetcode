class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        order = []
        for course, pre in prereq:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        completed = 0

        while q:
            node = q.popleft()
            order.append(node)
            completed += 1

            for course in graph[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        
        return order if completed == numCourses else []