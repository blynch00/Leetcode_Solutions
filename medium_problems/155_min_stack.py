class MinStack:

    def __init__(self):
        self.buckets = []
        self.smallest = []
        

    def push(self, val: int) -> None:
        if len(self.buckets) == 0:
            self.buckets.append(val)
            self.smallest.append(val)
        else:
            self.buckets.append(val)
            self.smallest.append(min(val, self.smallest[-1]))

    def pop(self) -> None:
        self.buckets.pop()
        self.smallest.pop()

    def top(self) -> int:
        return self.buckets[-1]

    def getMin(self) -> int:
        return self.smallest[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()