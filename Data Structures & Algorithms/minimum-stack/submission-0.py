class MinStack:

    def __init__(self):
        self._min = float("inf")
        self._stack = []

    def push(self, val: int) -> None:
        if not self._stack:
            self._stack.append(0)
            self._min = val
        else:
            self._stack.append(val - self._min)
            if val < self._min:
                self._min = val

    def pop(self) -> None:
        if not self._stack:
            return
        
        pop = self._stack.pop()
        if pop < 0:
            self._min = self._min - pop

    def top(self) -> int:
        top = self._stack[-1]
        if top > 0:
            return top + self._min
        else:
            return self._min

    def getMin(self) -> int:
        return self._min