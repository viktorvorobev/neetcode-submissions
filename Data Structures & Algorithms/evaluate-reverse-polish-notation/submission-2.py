class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        _stack = []
        operand_tokens = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in operand_tokens:
                _stack.append(int(token))
                continue
            right = _stack.pop()
            left = _stack.pop()
            result = int(float(eval(f"{left}{token}{right}")))
            _stack.append(result)
        return _stack[0]