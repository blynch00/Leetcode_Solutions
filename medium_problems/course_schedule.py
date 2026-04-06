from typing import List
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # BFS
        courses = deque()
        seen = set()

        for x in range(0, len(prerequisites)):
            if prerequisites[x][0] in seen:
                return False


sol = Solution()
preq = [[1,0],[0,1]]
print(sol.canFinish(2, preq))