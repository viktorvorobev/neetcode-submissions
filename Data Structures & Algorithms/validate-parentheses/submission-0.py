class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = ("()", "[]", "{}")
        for c in s:
            if not stack:
                stack.append(c)
                continue
            for left, right in pairs:
                if stack[-1] == left and c == right:
                    # valid pair
                    stack.pop()
                    break
            else:
                stack.append(c)
        return not stack
