from collections import *
class RecentCounter:

    def __init__(self):
        self.timers = deque()
    def ping(self, t: int) -> int:
        self.timers.append(t)
        while self.timers[0] < t-3000:
            self.timers.popleft()
        return len(self.timers)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)