class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        cal = []
        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/":
                a =cal.pop()
                b = cal.pop()
            if i == "+":
                cal.append(int(a+b))
            elif i == "-":
                cal.append(int(b-a))
            elif i == "*":
                cal.append(int(a*b))
            elif i == "/":
                cal.append(int(b/a))
            else:
                cal.append(int(i))
        return cal[0]