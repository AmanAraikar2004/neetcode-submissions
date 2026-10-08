class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                a = stack.pop()
                b = stack.pop()
                temp = b + a
                stack.append(temp)
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                temp = b - a
                stack.append(temp)
            elif i == "*":
                a = stack.pop()
                b = stack.pop()
                temp = b * a
                stack.append(temp)
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                temp = int(b / a)
                stack.append(temp)
            else:
                stack.append(int(i))
        return stack[-1]