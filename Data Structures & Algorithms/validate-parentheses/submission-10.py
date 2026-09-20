class Solution:
    def isValid(self, s: str) -> bool:
        """
        [[[[[]]]]]

        """
        stack = []
        if not s:
            return True
       
        for i in s :
            if i== "[":
                stack.append("]")
            elif i == "{":
                stack.append("}")
            elif i == "(":
                stack.append(")")
            elif stack and i == stack[-1]  :
                    stack.pop()
            else: # s=])} stack = [] # s = {}] s = {{{
                return False
                 
            # 如果相同,就pop,

        if not stack:
            return True
        else:
            return False

 