class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for rock in asteroids:

            while stack and stack[-1] > 0 and rock < 0:
                if stack[-1] < abs(rock):
                    stack.pop()
                    continue
                elif stack[-1] == abs(rock):
                    stack.pop()
                
                break
            else:
                stack.append(rock)
        return stack