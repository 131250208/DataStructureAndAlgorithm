class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()
        return x

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    minStack = MinStack()
    MinStack()
    minStack.push(0)
    minStack.push(1)
    minStack.push(0)
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.getMin())
