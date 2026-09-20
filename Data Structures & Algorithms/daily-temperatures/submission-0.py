class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pre_stack = []
        n =len(temperatures)
        result = [0] * n
        pre_stack.append(0)
        for i in range(1,n):
            
            while pre_stack and temperatures[i] > temperatures[pre_stack[-1]]:
                result[pre_stack[-1]] = i- pre_stack[-1]
                pre_stack.pop()
            
            
            pre_stack.append(i)
        return result


        #用单调栈